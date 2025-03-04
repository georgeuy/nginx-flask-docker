import express from 'express';


const app = express()


app.get('/', async (req, res, next) => {
    res.status(200).json({msg:'ok'})
});


app.listen(3001, () => console.log('Server running on port 3001'));