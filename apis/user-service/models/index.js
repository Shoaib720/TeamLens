// models/index.js
const { Sequelize, DataTypes } = require('sequelize');

// Initialize Sequelize with Connection String and Dialect
const sequelize = new Sequelize(process.env.MYSQL_CONNECTION_STRING, {
  dialect: 'mysql',
});

// Import each model and initialize it
const User = require('./user')(sequelize);
const Skill = require('./skill')(sequelize);

// Define UserSkill join table with a proficiency column
const UserSkill = sequelize.define('UserSkill', {
    proficiency: {
      type: DataTypes.ENUM('Beginner', 'Intermediate', 'Expert'),  // Allowed values
      allowNull: false,
      defaultValue: 'Beginner',
    },
  });

// Define a Many-to-Many relationship through the UserSkill table
User.belongsToMany(Skill, { through: UserSkill });
Skill.belongsToMany(User, { through: UserSkill });

// Export initialized models and Sequelize instance
module.exports = { sequelize, User, Skill };
