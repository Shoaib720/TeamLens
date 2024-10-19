const express = require('express');
const serverless = require('serverless-http');

// Initialize an Express app
const app = express();

// Define a simple GET route for the root path
app.get('/', (req, res) => {
  res.json({ message: 'Hello from Resources API' });
});

// Export the handler for AWS Lambda using serverless-http
module.exports.handler = serverless(app, {
    basePath: '/resources'
});
