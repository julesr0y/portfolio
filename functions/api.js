const express = require('express');
const serverless = require('serverless-http');
const app = express();
const router = express.Router();
const path = require('path');

app.use(express.static('dist'));

// Load View Engine
app.set('view engine', 'html');

router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

app.use('/.netlify/functions/api', router);
module.exports.handler = serverless(app);