import express from 'express';


const app = express()


app.get('/', async (req, res, next) => {
    res.status(200).json({msg:'hello from micro-2'})
});


app.listen(3000, () => console.log('Server running on port 3000'));