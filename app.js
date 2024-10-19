const express = require("express");
const bodyParser = require("body-parser");
const session = require("express-session");

const app = express();

// Middleware to parse URL-encoded data from forms
app.use(bodyParser.urlencoded({ extended: true }));

// Set up session management
app.use(
  session({
    secret: "mysecret", // Replace with a stronger secret in production
    resave: false,
    saveUninitialized: false,
  })
);

// Set the view engine to EJS
app.set("view engine", "ejs");

// User data for demo (replace with a database in real app)
const users = {
  user1: { username: "user1", password: "password123" },
};

// Routes
// GET: Render the login form
app.get("/login", (req, res) => {
  res.render("login");
});

// POST: Handle login
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  // Check if the user exists and the password matches
  if (users[username] && users[username].password === password) {
    // Save user info in session
    req.session.user = { username };
    res.redirect("/dashboard");
  } else {
    res.render("login", { error: "Invalid username or password" });
  }
});

// GET: Render the dashboard (protected route)
app.get("/dashboard", (req, res) => {
//   if (!req.session.user) {
//     return res.redirect("/login");
//   }
  dummy_user = {
    username: 'Shoaib Shaikh'
  }
//   res.render("dashboard", { user: req.session.user });
    res.render("dashboard", { user: dummy_user });
});

// GET: Logout and destroy session
app.get("/logout", (req, res) => {
  req.session.destroy(() => {
    res.redirect("/login");
  });
});

// Start the server
app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
