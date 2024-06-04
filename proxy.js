import bodyParser from 'body-parser';
import cors from 'cors';
import express from 'express';
import fetch from 'node-fetch';

const app = express();
const port = 3000;

app.use(cors({ origin: 'https://noyshoshan.i.ng' })); // Enable CORS for your domain
app.use(bodyParser.json());

app.post('/proxy', async (req, res) => {
    try {
        const response = await fetch('https://www.zohoapis.com/crm/v2/Leads', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer 1000.fe76cf37e7cc295362d15947bd43eaa5.a19e49d2da98392a75cead44be30f756', // השתמשי ב-Access Token שקיבלת
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(req.body)
        });

        const data = await response.json();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Proxy server running at http://localhost:${port}`);
});
