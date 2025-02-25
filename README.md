Your fantasy cricket project, built with Python and SQL, is a desktop-based application that allows users to create, manage, and evaluate fantasy cricket teams. Here’s an overview of its functionality:

Key Features:
Team Management

Users can create new teams by selecting players from a database.
The project enforces team composition rules, such as the number of batsmen, bowlers, all-rounders, and wicketkeepers.
Users can save and open teams stored in a MySQL database.
Database Integration

Player data (including category and value) is stored in a MySQL database (project_fantasy).
Teams and their player selections are also stored and retrieved from the database.
User Interface (UI) with PyQt5

The UI provides an interactive way for users to select and manage players.
Different sections display available players, team composition, and remaining points.
Users can switch between windows for creating, opening, and evaluating teams.
Fantasy Team Evaluation

Users can evaluate their fantasy team based on predefined metrics.
The EvaluateTeam module allows users to assess the strength of their team.
Point Management System

Each player has an assigned value, and users must create a team while staying within the allocated budget.
Main Python Files:
realproject.py: The main application file that initializes the UI and connects different components.
Openteam.py: Handles opening and managing saved teams from the database.
Evaluateteam.py: Provides team evaluation functionality.
Technologies Used:
Python (PyQt5) for the GUI.
MySQL for storing and retrieving player and team data.
Object-Oriented Programming (OOP) principles in Python.
