import { connect } from 'nats';

const listenNATS = async () => {
    const nc = await connect({ servers: ["ms7865:4222"] });

    const sub = nc.subscribe("stock.add");
    console.log("Listening for messages on 'stock.add'...");

    for await (const msg of sub) {
        console.log(`Received: ${msg.data.toString()}`);
    }
};

listenNATS();
