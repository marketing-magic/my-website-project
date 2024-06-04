import bodyParser from 'body-parser';
import express from 'express';
import fetch from 'node-fetch';

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/proxy', async (req, res) => {
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
});

app.listen(port, () => {
    console.log(`Proxy server running at http://localhost:${port}`);
});
