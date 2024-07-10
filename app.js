const http = require('http');
const express = require('express');
const path = require('path');
const app = express();
const helmet = require("helmet");

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));

app.use(helmet.contentSecurityPolicy({
    directives: {
        defaultSrc: ["'self'"],
        connectSrc: ["'self'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        scriptSrc: ["'self'", "'unsafe-inline'"],
        scriptSrcAttr: ["'unsafe-inline'"],
        mediaSrc: ["'self'"]
    }
})); // Middleware permettant de configurer la Content Security Policy (CSP) avec Helmet

// Home route.
app.get('/', (req, res) => {
    res.render('index');
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

const port = 3000;
const server = http.createServer(app);
server.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

module.exports = app;