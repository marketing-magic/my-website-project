import bodyParser from 'body-parser';
import cors from 'cors';
import express from 'express';
import fetch from 'node-fetch';

const app = express();
const port = 3000;

const client_id = "1000.A74ZA13YR9CIZEFNWB0PB4EK4SFX1B";
const client_secret = "32f017cf1fed5d7a01892c5f45ef0c04f48be50f89";
let access_token = "1000.9d2d76c07c12ac0ee9fe3d4b1b17481c.245561d1b2e1bd552a29370806c7fb72";
const refresh_token = "1000.6be3cc49e03e2e21bfe7083c30075985.56e6d7ea480c225933f75b533880c05c";

app.use(cors({ origin: 'https://noyshoshan.i.ng' }));
app.use(bodyParser.json());

async function refreshAccessToken() {
    try {
        const response = await fetch('https://accounts.zoho.com/oauth/v2/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                refresh_token: refresh_token,
                client_id: client_id,
                client_secret: client_secret,
                grant_type: 'refresh_token'
            })
        });

        const data = await response.json();
        access_token = data.access_token;
        console.log('Access token refreshed:', access_token);
    } catch (error) {
        console.error('Error refreshing access token:', error.message);
    }
}

app.post('/proxy', async (req, res) => {
    try {
        await refreshAccessToken();

        console.log('Received request:', req.body);

        const response = await fetch('https://www.zohoapis.com/crm/v2/Leads', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(req.body)
        });

        const data = await response.json();
        console.log('Response from Zoho:', data);
        res.json(data);
    } catch (error) {
        console.error('Error:', error.message);
        res.status(500).json({ error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Proxy server running at http://localhost:${port}`);
});
