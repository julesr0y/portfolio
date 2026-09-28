const express = require('express');
const path = require('path');
const app = express();
const helmet = require("helmet");
const links = require('./config/links.json');

// settings for view engine (ejs)
app.locals.links = links; // making links available in the views
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));

app.use(helmet.contentSecurityPolicy({
    directives: {
        defaultSrc: ["'self'"],
        connectSrc: ["'self'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        scriptSrc: ["'self'", "'unsafe-inline'", "https://www.google.com", "https://maps.googleapis.com", "https://cdnjs.cloudflare.com"],
        scriptSrcAttr: ["'unsafe-inline'"],
        mediaSrc: ["'self'"],
        imgSrc: ["'self'", "data:", "https://maps.gstatic.com", "https://maps.googleapis.com", "https://www.google.com"],
        frameSrc: ["'self'", "https://www.google.com", "https://www.google.fr", "https://maps.google.com"],
        childSrc: ["'self'", "https://www.google.com", "https://www.google.fr", "https://maps.google.com"],
    }
})); // middleware for Content Security Policy (CSP)

// home route
app.get('/', (req, res) => {
    res.render('index');
});

// projects route
app.get('/projects', (req, res) => {
    res.render('projects');
});

// 404 route
app.use((req, res, next) => {
    res.status(404).render('404');
});

// error handling
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

module.exports = app;