// skillRoutes.js
const express = require('express');
const { Skill, User } = require('../models');

const router = express.Router();

// Create a new skill
router.post('/', async (req, res) => {
  try {
    const { name } = req.body;
    const skill = await Skill.create({ name });
    res.status(201).json({ message: 'Skill created', skill });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Assign a skill to a user
router.post('/assign', async (req, res) => {
  try {
    const { userId, skillId, proficiency } = req.body;

    const user = await User.findByPk(userId);
    const skill = await Skill.findByPk(skillId);

    if (!user || !skill) {
      return res.status(404).json({ error: 'User or Skill not found' });
    }

    await user.addSkill(skill, { through: { proficiency } });
    res.json({ message: 'Skill assigned to user' });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get skills of a user
router.get('/user/:id', async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id, {
      include: Skill,
    });

    if (!user) return res.status(404).json({ error: 'User not found' });

    res.json({ user: user.id, skills: user.Skills });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get users with a specific skill
router.get('/skill/:id', async (req, res) => {
  try {
    const skill = await Skill.findByPk(req.params.id, {
      include: {
        model: User,
        attributes: { exclude: ['password'] },  // Exclude password
        through: { attributes: ['proficiency'] },  // Include proficiency level
      },
    });

    if (!skill) return res.status(404).json({ error: 'Skill not found' });

    res.json({ skill: skill.name, users: skill.Users });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

router.delete('/unassign', async (req, res) => {
    try {
        const { userId, skillId } = req.body;

        const user = await User.findByPk(userId);
        const skill = await Skill.findByPk(skillId);

        if (!user || !skill) {
            return res.status(404).json({ error: 'User or Skill not found' });
        }

        // Remove the skill association from the user
        await user.removeSkill(skill);
        res.json({ message: 'Skill unassigned from user' });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get all skills
router.get('/', async (req, res) => {
    try {
        const skills = await Skill.findAll();
        res.json(skills);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});
  
// Delete a skill by ID
router.delete('/:skillId', async (req, res) => {
    try {
        const skill = await Skill.findByPk(req.params.skillId);
        if (!skill) {
            return res.status(404).json({ error: 'Skill not found' });
        }
  
        await skill.destroy();
        res.json({ message: 'Skill deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

module.exports = router;
