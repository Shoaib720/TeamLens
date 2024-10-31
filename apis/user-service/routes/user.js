// userRoutes.js
const express = require('express');
const bcrypt = require('bcryptjs');
const { User } = require('../models'); // Assuming User model is in models.js or index.js if defined with sequelize

const router = express.Router();

// Create a new user
router.post('/', async (req, res) => {
  try {
    const { userid, name, password, experience, role } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = await User.create({ userid, name, password: hashedPassword, experience, role });
    res.status(201).json({ message: 'User created', user });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get all users
router.get('/', async (req, res) => {
  try {
    const users = await User.findAll({ attributes: { exclude: ['password'] } });
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get a user by userid
router.get('/:id', async (req, res) => {
  try {
    const user = await User.findOne({
      where: { id: req.params.id },
      attributes: { exclude: ['password'] },
    });
    if (!user) return res.status(404).json({ error: 'User not found' });
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Update a user
router.put('/:id', async (req, res) => {
  try {
    const { name, password, experience, role, isAdmin } = req.body;
    const user = await User.findOne({ where: { id: req.params.id } });
    if (!user) return res.status(404).json({ error: 'User not found' });

    user.name = name || user.name;
    if (password) user.password = await bcrypt.hash(password, 10);
    user.experience = experience || user.experience;
    user.role = role || user.role;
    user.isAdmin = isAdmin || user.isAdmin;

    await user.save();
    res.json({ message: 'User updated', user });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a user
router.delete('/:id', async (req, res) => {
  try {
    const result = await User.destroy({ where: { id: req.params.id } });
    if (!result) return res.status(404).json({ error: 'User not found' });
    res.json({ message: 'User deleted' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
