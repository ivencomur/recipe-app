Recipe App – A Django Web Application

A Comprehensive Journey from Command-Line Script to Deployed Web App

Student: Ivan Cortes
Course: CareerFoundry – Python for Web Developers

Status: ✅ Achievement 2 Complete & Deployed!
Live Site: https://recipe-app-ivan-cortes-8d505e6123c3.herokuapp.com/

Last Updated: October 22, 2025

1. Project Overview

Welcome to my Recipe App! This project is the culmination of my learning journey through the CareerFoundry Python for Web Developers course. What began as a series of command-line scripts in Achievement 1 has been progressively built into a full-stack, database-driven web application using the Django framework.

This repository serves as a portfolio piece and a detailed record of the development process. It documents the evolution of the application, from initial project setup and database modeling to the implementation of user authentication, advanced search, data visualization, and finally, a successful production deployment. It is a practical showcase of the Model-View-Template (MVT) architecture and a testament to the real-world challenges—and solutions—involved in bringing a web application to life.

Final Features:

Multi-App Structure: A clean, modular project with distinct Django apps for recipes (recipes), the homepage (sales), and other components.

Database-Driven Recipes: A full application with recipes and ingredients stored in a persistent PostgreSQL database in production.

User Authentication: A secure login/logout system that protects content, ensuring only logged-in users can view recipe details.

Advanced Search & Filtering: A dedicated search page allowing users to filter recipes by name, ingredients (with OR logic), cooking time, and difficulty.

Dynamic Data Visualization: On-the-fly generation of bar, pie, and line charts using pandas and matplotlib based on live search results.

Production Deployment: Successfully deployed to Heroku with a PostgreSQL database, Gunicorn as the web server, and WhiteNoise for efficient static file serving.

Professional Styling: A consistent and clean user interface across all pages, including a homepage, recipe lists, detail views, and an "About Me" page.

2. The Project Journey: From a Script to a Live Application

This project was built incrementally, with each exercise adding a new layer of functionality. This summary is based on the detailed Learning Journals kept throughout the process.

Achievement 1: Python Fundamentals

Exercise 1.1 - 1.2: The Basics - Environment and Data Structures

Goal: Establish a Python development environment and structure the initial data.

What I Did: Set up a virtual environment (venv) to manage dependencies. I chose to model recipes using a list of dictionaries, a flexible pattern where each dictionary holds a recipe's name, cooking_time, and ingredients.

Key Skill: Environment isolation and basic data modeling in Python.

Exercise 1.3: Bringing Logic to Life with Functions and Control Flow

Goal: Build an interactive script that could collect recipe data.

What I Did: Wrote my first functions, used loops to collect multiple recipes from user input, and implemented conditionals (if/elif/else) to calculate a recipe's difficulty. This is where the code started to feel like a real program.

Key Challenge: A persistent IndentationError taught me a crucial lesson about Python's reliance on whitespace for structure.

Exercise 1.4: Making Data Persistent with File Handling

Goal: Save the collected recipes so they wouldn't be lost when the program closed.

What I Did: I implemented file handling to save the recipe list to a binary file (.bin) using Python's pickle module. I also wrote robust try...except blocks to handle FileNotFoundError, allowing the program to create a new file if one didn't exist.

Key Skill: Data persistence and defensive programming with error handling.

Exercise 1.5 - 1.7: OOP, Databases, and ORM

Goal: Refactor the code using professional patterns like Object-Oriented Programming and a real database.

What I Did: I refactored the app using OOP, creating a Recipe class that turned recipes into smart objects with their own data and methods. Then, I replaced the pickle file with a MySQL database, learning to perform CRUD operations with raw SQL. A critical lesson was learning to prevent SQL injection by using parameterized queries. Finally, I was introduced to Object-Relational Mapping (ORM) with SQLAlchemy, which replaced my raw SQL strings with more Pythonic, object-oriented code.

Key Skill: Understanding the progression from procedural code to OOP, and from raw SQL to the abstraction of an ORM.

Achievement 2: Building a Full-Stack Web Application with Django

Exercise 2.2 - 2.3: The Django Foundation & The ORM

Goal: Set up a Django project and design the database schema using Django's powerful ORM.

What I Did: I created the recipe_project, learned the difference between a Django "project" and an "app," and defined my database schema in recipes/models.py. I created Recipe, Ingredient, and the crucial RecipeIngredient models, using ManyToManyField with a through table to store quantities and units. I then used makemigrations and migrate to build the database and explored the Django Admin for data entry.

Key Skill: Translating a real-world schema into Django Models and mastering the migration workflow.

Exercise 2.4 - 2.5: Views, Templates, and Dynamic URLs

Goal: Display the recipe data on actual web pages.

What I Did: I wrote my first Views (both Function-Based and Class-Based) to handle web requests and fetch data. I created Templates using HTML and the Django Template Language (DTL) to display the data dynamically. I implemented a ListView for all recipes and a DetailView for individual ones, using get_absolute_url to create dynamic links between them.

Key Challenge: The TemplateDoesNotExist error was a valuable lesson in Django's strict but logical app/templates/app/ directory convention.

Exercise 2.6: Implementing User Authentication

Goal: Secure the recipe pages so only logged-in users could access them.

What I Did: I leveraged Django's built-in authentication system to create a full login/logout flow. I protected my views with LoginRequiredMixin and used the user.is_authenticated variable in templates to show different content to logged-in vs. logged-out users.

Key Skill: Implementing a complete and secure user authentication and authorization flow.

Exercise 2.7: Forms and Data Visualization

Goal: Allow users to search for recipes and visualize the results.

What I Did: I built a RecipeSearchForm using Django's Forms API. The search view processes user input to filter recipes using Q objects for complex OR queries. The highlight was integrating pandas and matplotlib to generate charts from the filtered data, converting them to base64 strings to embed directly in the HTML.

Key Challenge: Making matplotlib work on a web server required setting its backend to 'Agg' to prevent it from trying to open a GUI window.

Exercise 2.8: Going Live with Production Deployment

Goal: Deploy the application to a live server on Heroku.

What I Did: This was a massive undertaking. I configured the project for production by moving secrets to environment variables (python-decouple), setting DEBUG=False, and adding security settings. I set up Gunicorn as the web server, WhiteNoise for static files, and created the necessary Procfile and runtime.txt for Heroku. The biggest challenges were migrating to a paid PostgreSQL database and writing a custom script to fix character encoding issues (UnicodeDecodeError) when importing my local data. I also implemented a workaround for Heroku's ephemeral filesystem by changing the image field to a CharField and using placeholder URLs.

Key Skill: Configuring a Django app for a production environment and troubleshooting complex, real-world deployment issues.

3. Live Application & Access

The final, deployed application is live and can be accessed at the following URL:

https://recipe-app-ivan-cortes-8d505e6123c3.herokuapp.com/

Credentials for Review:

Username: mentorCF

Password: Ment0r@CareerF0undry

(Please note: Recipe images are currently placeholders due to Heroku's ephemeral filesystem, a common architectural constraint addressed in the deployment.)

4. Technical Stack & Environment

Python: 3.13.5

Django: 5.2.7

Database (Local): SQLite

Database (Production): PostgreSQL

Key Libraries: gunicorn, whitenoise, python-decouple, dj-database-url, psycopg2-binary, pandas, matplotlib, Pillow.

Deployment Platform: Heroku

Development Environment: Windows / Git Bash / VS Code

5. Local Installation & Setup

To run this project on your own machine, follow these steps:

# 1. Clone the repository from GitHub
git clone [https://github.com/ivencomur/recipe-app.git](https://github.com/ivencomur/recipe-app.git)
cd recipe-app

# 2. Create and activate a Python virtual environment
# (Ensure you are using Python 3.13 or a compatible version)
python -m venv .venv
source .venv/Scripts/activate  # Command for Git Bash on Windows

# 3. Install all the required packages
pip install -r requirements.txt

# 4. Create a local .env file for environment variables
#    Create a file named .env in the root and add:
#    SECRET_KEY='a_new_secret_key'
#    DEBUG=True
#    DATABASE_URL='sqlite:///db.sqlite3'
#    ALLOWED_HOSTS='127.0.0.1,localhost'

# 5. Apply the database migrations to create your local db.sqlite3 file
python manage.py migrate

# 6. Create a local superuser to access the admin panel
python manage.py createsuperuser

# 7. (Optional) Load the initial recipe data
# This will populate your local database with the 22 recipes from the project.
python manage.py loaddata recipes_data_utf8.json

# 8. Start the local development server!
python manage.py runserver


You can now access the application at http://127.0.0.1:8000/.

6. Testing

The project includes a suite of unit tests to ensure functionality and prevent regressions.

Model Tests: Verify database constraints, relationships, and model methods.

Form Tests: Ensure the RecipeSearchForm validates input correctly.

View Tests: Check that views require authentication, handle GET/POST requests, filter data correctly, and pass the right context to templates.

To run the tests, execute the following command from the root directory:

python manage.py test recipes

All tests pass successfully. A screenshot of the passing test report (test-report.jpg) is included in the PYTHON-ACHIEVEMENT-2/EXERCISE-2.8/screenshots/ repository folder.

7. Author & Links
Ivan Cortes

Portfolio: https://ivan-cortes-portfolio-v1.onrender.com/

LinkedIn: https://www.linkedin.com/in/ivan-cortes-murcia-22053953/

GitHub: https://github.com/ivencomur

8. References and Documentation
Throughout this project, a variety of official documentation and resources were essential for learning and troubleshooting.

Achievement 1
Python Official Documentation: For core language features, functions, and standard library modules.

MySQL Documentation: For SQL syntax and server setup.

SQLAlchemy Documentation: For understanding ORM patterns and version differences.

Achievement 2
Django Documentation: The primary resource for everything from models and views to forms and deployment.

Django Project Website

Models & Database Layer

Views & Templates

Authentication System

Django Forms

Deployment Checklist

Heroku Dev Center: Essential for platform-specific commands and troubleshooting.

Getting Started on Heroku with Python

Configuring Django Apps for Heroku

Third-Party Libraries:

Gunicorn: For understanding the production WSGI server.

WhiteNoise: For static file serving configuration.

python-decouple: For environment variable management.

dj-database-url: For parsing database URLs.

Pandas & Matplotlib: For data visualization.
