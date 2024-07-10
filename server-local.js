'use strict';
const express = require('express');
const app = require('./express/server');
const path = require('path');

app.use(express.static('public'));

// Load View Engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'html');

// Local request handlers.
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route Files.
// let page1 = require('./routes/page1');
// let page2 = require('./routes/page2');
// let page3 = require('./routes/page3');
// let page4 = require('./routes/page4');
// app.use('/page1', page1);

// Start Server.
let port = 3000;
app.listen(port, function () {
    console.log(`Server started on port ${port}...`);
});