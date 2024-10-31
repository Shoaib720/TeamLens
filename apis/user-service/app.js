// index.js
require('dotenv').config();
const express = require('express');
const {sequelize} = require('./models')
const userRoutes = require('./routes/user'); // Import userRoutes
const skillRoutes = require('./routes/skill')

const app = express();
app.use(express.json());

// Sync or authenticate depending on environment
if (process.env.NODE_ENV !== 'production') {
  sequelize.sync({ alter: true })
    .then(() => console.log('Database synced'))
    .catch(err => console.error('Sync error:', err));
} else {
  sequelize.authenticate()
    .then(() => console.log('Database connected'))
    .catch(err => console.error('Connection error:', err));
}

// Use the user routes with the /api/v1/users prefix
app.use('/api/v1/users', userRoutes);
app.use('/api/v1/skills', skillRoutes);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
