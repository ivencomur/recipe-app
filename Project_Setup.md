Recipe App - Project Setup Guide

📋 Complete File Structure

This document provides a complete guide to setting up the Recipe App Django project from the repository.

🏗️ Required Files

Root Directory Files

manage.py - Django management script

README.md - Project documentation

requirements.txt - Python dependencies

.gitignore - Git ignore file

index.html - Learning journey documentation

LEARNING_JOURNAL/ - Folder containing all journal entries for Achievements 1 & 2.

Project Configuration (recipe_project/)

__init__.py - Package initializer

settings.py - Django settings

urls.py - URL configuration

wsgi.py - WSGI configuration

asgi.py - ASGI configuration

Apps Structure

Each app should have these files:

__init__.py - Package initializer

apps.py - App configuration

models.py - Database models

admin.py - Admin interface

views.py - View functions

tests.py - Unit tests

migrations/ - Migration directory

__init__.py - Package initializer

Migration files (auto-generated)

📦 App-Specific Files

recipes/

models.py - Contains Recipe, Ingredient, and RecipeIngredient models.

admin.py - Admin configuration with inline editing.

views.py - Contains RecipeListView and RecipeDetailView.

urls.py - URL routing for the recipes app.

templates/recipes/ - Contains recipes_list.html and recipes_detail.html.

tests.py - Comprehensive model and URL tests.

books/

models.py - Book model with genre and type choices.

admin.py - Book admin with search and filters.

tests.py - Book model validation tests.

sales/

views.py - Contains the home view for the main landing page.

urls.py - URL routing for the sales app (homepage).

templates/sales/ - Contains recipes_home.html.

customers/

models.py - Customer model with notes.

admin.py - Simple customer admin.

salespersons/

models.py - Salesperson model with unique username.

admin.py - Salesperson admin with search.

🚀 Setup Instructions

1. Clone and Navigate

git clone [https://github.com/ivencomur/recipe-app.git](https://github.com/ivencomur/recipe-app.git)
cd recipe-app


2. Create Virtual Environment

# Windows
python -m venv venv
source venv/Scripts/activate  # Git Bash
# or
venv\Scripts\activate.bat  # Command Prompt

# Mac/Linux
python -m venv venv
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Create and Apply Migrations

# Create migration files for all apps
python manage.py makemigrations

# Apply migrations to create database tables
python manage.py migrate


5. Create Superuser

python manage.py createsuperuser
# Follow prompts to set username, email, and password


6. Run Tests

# Run all tests
python manage.py test

# Run tests for specific apps
python manage.py test recipes


7. Start Development Server

python manage.py runserver
# Server starts at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


8. Access the Application

Navigate to http://127.0.0.1:8000/ to see the homepage.

Navigate to http://127.0.0.1:8000/recipes/ to see the recipe list.

Navigate to http://127.0.0.1:8000/admin/ to log in and manage data.

🧪 Testing the Setup

Quick Verification Checklist

[ ] Virtual environment activated

[ ] Django and Pillow installed (check with pip list)

[ ] All apps listed in INSTALLED_APPS

[ ] Migrations applied successfully

[ ] Admin interface accessible

[ ] All models visible in admin

[ ] Tests passing for all apps

🐛 Common Issues and Solutions

Issue: ModuleNotFoundError

Solution: Ensure virtual environment is activated and all packages from requirements.txt are installed.

Issue: TemplateDoesNotExist

Solution: Verify the template path is correct: app_name/templates/app_name/template.html.

Issue: 404 Not Found

Solution: Check that the URL is defined in the correct urls.py file (project or app) and that the project urls.py includes the app's URLs.

📚 Next Steps

Exercise 2.6 - Django Forms

Create forms to allow users to add and edit recipes from the front end.

Handle POST requests and validate user input.

Implement CRUD (Create, Read, Update, Delete) functionality.

And Beyond

User authentication

Data analysis and visualization

Production deployment

Last Updated: October 2025 Course: CareerFoundry - Python for Web Developers Repository: https://github.com/ivencomur/recipe-app