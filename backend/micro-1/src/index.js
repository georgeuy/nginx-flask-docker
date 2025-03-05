import express from 'express';
import { connect } from 'nats';

const app = express()

app.use(express.json())

let nc;

// Conectar a NATS antes de que el servidor empiece a recibir peticiones
const startNATS = async () => {
    
    nc = await connect({ servers: ["nats:4222"] });
    console.log("Connected to NATS");

    // Suscribirse a "stock.add" sin bloquear el código
    nc.subscribe("stock.add", {
        callback: (err, msg) => {
            if (err) {
                console.error("Error receiving message:", err);
                return;
            }
            console.log(`Received message on 'stock.add': ${msg.data.toString()}`);
        }
    });

    console.log("Listening for messages on 'stock.add'...");
};

const products = [
    {id:1, name:'apple'},
    {id:2, name:'orange'},
]


app.get('/', async (req, res, next) => {
    res.status(200).json({
        success: true,
        data: products
    });
});

app.post('/', async (req, res, next) => {

    try{

        const product = req.body;

        //add product to stock
        products.push(product)

        // Publicar el mensaje en un subject, por ejemplo "stock.add"
        nc.publish("stock.add", JSON.stringify(product));

        //send response back to the client
        res.status(201).json({
            success: true,
            data: product
        });

    }catch(err){
        console.log(err)
        res.status(500).json({success:false, error:'Error al agregar un item al stock'})
    }

});

// Iniciar el servidor después de conectar a NATS
startNATS().then(()=>{
    app.listen(3000, () => console.log('Server running on port 3000'));    
}).catch(err => console.log("Error connecting to NATS: ",err.message))

