import bodyParser from 'body-parser';
import cors from 'cors'; // Import CORS
import express from 'express';
import fetch from 'node-fetch';

const app = express();
const port = 3000;

app.use(cors()); // Enable CORS
app.use(bodyParser.json());

app.post('/proxy', async (req, res) => {
    try {
        const response = await fetch('https://www.zohoapis.com/crm/v2/Leads', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer YOUR_ACCESS_TOKEN', // החליפי את YOUR_ACCESS_TOKEN ב-Access Token שקיבלת
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
