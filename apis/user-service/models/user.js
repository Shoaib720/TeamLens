// models/user.js
const { DataTypes } = require('sequelize');
const bcrypt = require('bcryptjs');

// Function to define the User model
module.exports = (sequelize) => {
  const User = sequelize.define('User', {
    name: { 
      type: DataTypes.STRING, 
      allowNull: false 
    },
    password: { 
      type: DataTypes.STRING, 
      allowNull: false 
    },
    experience: { 
      type: DataTypes.DECIMAL(2, 1), 
      allowNull: false 
    },
    role: { 
      type: DataTypes.STRING, 
      allowNull: false 
    },
    isAdmin: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        default: false
    }
  });

  // Hash password before saving the user
  User.beforeCreate(async (user) => {
    if (user.password) {
      user.password = await bcrypt.hash(user.password, 10);
    }
  });

  User.beforeUpdate(async (user) => {
    if (user.password) {
      user.password = await bcrypt.hash(user.password, 10);
    }
  });

  return User;
};
