Recipe App - Django Web Application

📚 Python for Web Developers - Achievement 2

Student: Ivan Cortes

Course: CareerFoundry - Python for Web Developers

Repository: Django-based Recipe Management System

🎯 Project Overview

This Django web application is the evolution of the command-line Recipe App from Achievement 1. It demonstrates the transition from CLI to a full web-based application using Django's MVT architecture.

Current Features (Exercise 2.5)

✅ Django project structure with multiple apps

✅ Recipe management with ingredients (Many-to-Many relationships)

✅ (New) Image uploads for recipes with media file handling

✅ (New) Dynamic, styled front-end pages for recipe lists and details

✅ Book inventory system (from bookstore example)

✅ Sales tracking with customers and salespersons

✅ SQLite database with migrations

✅ Django admin interface configured

✅ Comprehensive model and URL testing

📁 Project Structure

recipe-app/
├── recipe_project/          # Main Django project folder
│   ├── settings.py
│   └── urls.py
│
├── recipes/                 # Recipe management app
│   ├── migrations/
│   ├── templates/recipes/   # HTML templates for the app
│   │   ├── recipes_list.html
│   │   └── recipes_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py              # App-specific URL routing
│   └── views.py
│
├── media/                   # Stores user-uploaded images
│
├── sales/                   # App for the homepage
│
├── books/                   # (Example app)
├── customers/               # (Example app)
├── salespersons/            # (Example app)
│
├── manage.py                # Django management script
├── db.sqlite3               # SQLite database
├── requirements.txt         # Python dependencies
└── .gitignore               # Git ignore file


🛠️ Installation & Setup

Prerequisites

Python 3.8 or higher

pip (Python package manager)

Git

Step 1: Clone the Repository

git clone [https://github.com/ivencomur/recipe-app.git](https://github.com/ivencomur/recipe-app.git)
cd recipe-app


Step 2: Create Virtual Environment

# Windows (Git Bash)
python -m venv .venv
source .venv/Scripts/activate


Step 3: Install Dependencies

pip install -r requirements.txt


Step 4: Run Migrations

python manage.py migrate


Step 5: Create Superuser (for Admin Access)

python manage.py createsuperuser


Step 6: Run Development Server

python manage.py runserver


Visit: http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/

📊 Data Models

Recipe App Models

Recipe Model

name: CharField (recipe name)

description: TextField (recipe instructions)

cook_time_minutes: PositiveIntegerField (cooking time)

pic: ImageField (recipe picture) (New)

ingredients: ManyToManyField (through RecipeIngredient)

created_at: DateTimeField (auto-added)

Ingredient Model

name: CharField (unique ingredient name)

RecipeIngredient Model (Junction Table)

recipe: ForeignKey to Recipe

ingredient: ForeignKey to Ingredient

quantity: FloatField (amount needed)

unit: CharField (measurement unit)

Book Inventory Models

Book Model

name: CharField

author_name: CharField

price: FloatField (in USD)

genre: CharField with choices

book_type: CharField with choices

Customer & Sales Models

Customer: name and notes

Salesperson: username, name, and bio

🧪 Running Tests

Run All Tests

python manage.py test


Run Tests for Specific App

python manage.py test recipes


Test Coverage

✅ Model field validations

✅ Model string representations

✅ Default values

✅ Field constraints (max_length, validators)

✅ Unique constraints

✅ Many-to-Many relationships

✅ (New) get_absolute_url() method for correct URL generation.

🎓 Learning Journey

Exercise 2.1 - Getting Started with Django

Set up development environment and installed Django.

Learned MVT architecture.

Exercise 2.2 - Django Project Structure

Created Django project and multiple apps.

Designed database models and configured admin.

Exercise 2.3 - Django Models

Implemented models.py for all apps.

Used the migration system (makemigrations, migrate).

Customized the Django admin for a better UI.

Exercise 2.4 - Django Views & Templates

Created a Function-Based View (FBV) and a template for the homepage.

Set up initial project and app URL routing.

Exercise 2.5 - Django MVT Revisited (Current)

Configured the project to handle user-uploaded images (media files).

Implemented Class-Based Views (ListView, DetailView).

Created dynamic templates to display database content.

Enabled clickable links between list and detail pages using get_absolute_url.

Upcoming Exercises

Exercise 2.6: Django Forms

Exercise 2.7: User Authentication

Exercise 2.8: Deployment

💡 Key Django Concepts Applied

MVT Architecture

Models: Database structure (recipes, ingredients, books)

Views: Business logic implemented with Function-Based and Class-Based Views. (Updated)

Templates: HTML presentation with dynamic data via Django Template Language. (Updated)

Django ORM

Model definitions with field types

Model relationships (ForeignKey, ManyToMany)

Migrations for database schema changes

QuerySets for database queries

Django Admin

Automatic admin interface generation

Model registration with customization

List display, search, and filters

Inline editing for related models

🐛 Known Issues & TODOs

Current TODOs

[x] Implement views for recipe listing and details

[x] Create HTML templates for user interface

[x] Add URL routing for all apps

[x] Implement recipe image uploads

[ ] Implement recipe search functionality

[ ] Add recipe difficulty calculation

[ ] Create forms for recipe creation/editing

[ ] Add user authentication

Future Enhancements

Recipe categories and tags

User favorites and ratings

Shopping list generation

Meal planning features

Nutrition information

Recipe sharing functionality

📚 Resources

Documentation

Django Official Documentation

Django Tutorial

Django Models Reference

Django Admin Documentation

Course Materials

CareerFoundry Python for Web Developers

Achievement 2 Exercise Materials

Course Repository

🤝 Contributing

This is a learning project for CareerFoundry's Python course. While it's primarily for educational purposes, feedback and suggestions are welcome!

Development Workflow

Create feature branch from main

Make changes and test locally

Run tests to ensure nothing breaks

Commit with descriptive messages

Push and create pull request

📝 License

This project is part of CareerFoundry's educational curriculum and is for learning purposes.

👤 Author

Ivan Cortes

Portfolio: ivan-cortes-portfolio-v1.onrender.com

LinkedIn: Ivan Cortes Murcia

GitHub: @ivencomur

Twitter: @IVENCOMUR

🙏 Acknowledgments

CareerFoundry for the comprehensive curriculum

Django Software Foundation for the excellent framework

Python community for extensive documentation and support

📸 Screenshots

Django Admin Interface

Coming soon: Screenshots of the admin interface showing recipe and book management

Project Structure in VS Code

Coming soon: IDE view showing the organized project structure

Test Results

Coming soon: Terminal output showing successful test runs

🔧 Technical Stack

Language: Python 3.13.5

Framework: Django 5.2.7

Database: SQLite (development)

Version Control: Git/GitHub

IDE: VS Code

Testing: Django's built-in TestCase

Last Updated: October 2025
Course: CareerFoundry - Python for Web Developers
Achievement 2 - Web Development with Django