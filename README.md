# Recipe App – Django Web Application

_Achievement 2 • CareerFoundry – Python for Web Developers_

**Student:** Ivan Cortes
**Repository:** `recipe-app` (Django-based Recipe Management System)
{/* */}
**Current Exercise:** 2.8 - Deployment (Next Step)
{/* */}
**Last Updated:** October 19, 2025

---

## Table of Contents
1. [Overview](#overview)
2. [Learning Objectives](#learning-objectives)
3. [Environment & Specs](#environment--specs)
4. [Project Structure](#project-structure)
5. [Installation & Setup (Windows + Git Bash)](#installation--setup-windows--git-bash)
6. [Running the App](#running-the-app)
7. [Authentication & Access Control](#authentication--access-control)
8. [Data Models](#data-models)
9. [Testing](#testing)
10. [Development Workflow](#development-workflow)
11. [Known Issues & TODOs](#known-issues--todos)
12. [Future Enhancements](#future-enhancements)
13. [Resources](#resources)
14. [Deliverables](#deliverables)
15. [Technical Notes](#technical-notes)
16. [Author & Links](#author--links)
17. [AI Assistance Note](#ai-assistance-note)
18. [Screenshots List](#screenshots-list)

---

## Overview
This Django web application evolves the command‑line Recipe App from **Achievement 1** into a full web application following Django’s **MVT** (Model–View–Template) architecture. This project serves as the practical implementation for Achievement 2 of the CareerFoundry Python for Web Developers course.

{/* */}
**Current scope (Completion of Exercise 2.7):**
- Project with multiple Django apps (`recipes`, `sales`, `books`, etc.).
- Recipe Management: Display of recipes with images and ingredients (via Many‑to‑Many `through` model). Media file handling configured.
- User Authentication: Secure login/logout using Django's auth system. Recipe list, detail, and search views are protected.
- Search & Filtering: A functional search page (`/recipes/search/`) allows filtering recipes by name, ingredients (OR logic), max cooking time, and difficulty via `RecipeSearchForm`.
- Data Visualization: Dynamic generation and embedding of charts (bar, pie, line) based on search results using `pandas` and `matplotlib`.
- Database & Admin: SQLite database managed via ORM and migrations. Models registered in Django Admin.
- Testing: Unit tests cover models, URLs, forms (Ex 2.7), and views (Ex 2.7).

---

## Learning Objectives
By the end of Achievement 2, key objectives include:
- Implementing Django’s MVT pattern.
- Designing and migrating database models with relationships.
- Configuring and handling static and media files.
- Building FBVs and CBVs (`ListView`, `DetailView`).
- Implementing user authentication and view protection.
- Mastering URL routing including namespacing and dynamic URLs.
{/* */}
- Creating and processing Django Forms.
- Integrating data visualization libraries.
- Writing comprehensive tests for various components.
{/* */}
- Upcoming: Deploying a Django application to a live server.

---

## Environment & Specs
- **Python:** 3.13.5 (Virtual environment `.venv`)
- **Django:** 5.2.7
- **Database:** SQLite (development)
{/* */}
- **Key Libraries:** `Pillow`, `pandas`, `matplotlib`
- **OS/Shell:** Windows / Git Bash
- **IDE:** VS Code
- **Version Control:** Git / GitHub

> Activate virtual environment: `source .venv/Scripts/activate`

---

## Project Structure
```text
recipe-app/
├── .venv/
├── recipe_project/
│   ├── settings.py
│   ├── urls.py
│   └── views.py (auth)
│
├── recipes/
│   ├── migrations/
{/* */}
│   ├── templates/recipes/ (list, detail, search)
{/* */}
│   ├── tests/ (incl. test_forms.py, test_views.py)
│   ├── admin.py
{/* */}
│   ├── forms.py (RecipeSearchForm)
{/* */}
│   ├── models.py (Recipe incl. difficulty)
{/* */}
│   ├── urls.py (incl. search)
{/* */}
│   └── views.py (ListView, DetailView, recipe_search, generate_recipe_chart)
│
├── sales/ (homepage)
│   └── ...
│
├── templates/ (project-level auth)
│   └── auth/
│
├── media/ (user uploads)
│
├── books/, customers/, salespersons/ (example apps)
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
{/* */}
└── requirements.txt (incl. pandas, matplotlib)

# LEARNING_JOURNAL/ (Sibling directory likely)
#   ├── LEARNING_JOURNAL_2.7_(14).html
#   └── ...

# PYTHON-ACHIEVEMENT-2/ (Separate repo likely)
#   └── Exercise 2.7/screenshots/
#       └── ...
(Structure reflects completed Exercise 2.7)

Installation & Setup (Windows + Git Bash)
git clone https://github.com/ivencomur/recipe-app.git && cd recipe-app

python -m venv .venv

source .venv/Scripts/activate {/* */}

pip install -r requirements.txt (Ensure pandas & matplotlib are listed)

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Running the App
Homepage: http://127.0.0.1:8000/

Login: http://127.0.0.1:8000/login/

Recipe List: http://127.0.0.1:8000/recipes/ (Login required)

Recipe Detail: e.g., http://127.0.0.1:8000/recipes/1/ (Login required) {/* */}

Recipe Search: http://127.0.0.1:8000/recipes/search/ (Login required)

Admin: http://127.0.0.1:8000/admin/

Authentication & Access Control
Uses django.contrib.auth.

Project-level views handle /login/, /logout/. {/* */}

RecipeListView, RecipeDetailView, recipe_search are protected (LoginRequiredMixin or @login_required).

LOGIN_URL = '/login/' redirects unauthenticated users.

Templates use user.is_authenticated for conditional display.

Data Models
(Primary models)

Recipe: Includes name, description, cook_time_minutes, pic, ingredients (M2M via RecipeIngredient), difficulty, created_at.

Ingredient: Includes name (unique).

RecipeIngredient: Links Recipe and Ingredient with quantity and unit. unique_together constraint.

Testing
Run with: python manage.py test recipes (or python manage.py test recipes.tests) {/* */}

Covers models (validation, relationships, get_absolute_url), forms (Ex 2.7), and views (auth, filtering, context - Ex 2.7).

Development Workflow
(Standard Git flow: branch -> code -> test -> commit -> push -> merge)

Known Issues & TODOs
{/* */}

[x] Implement recipe list/detail views (Ex 2.5)

[x] Create HTML templates for UI (Ex 2.4, 2.5, 2.7)

[x] Add URL routing for all apps (Ex 2.4, 2.5, 2.6, 2.7)

[x] Implement recipe image uploads (Ex 2.5)

[x] Add User Authentication & Protect Views (Ex 2.6)

[x] Add difficulty field to Recipe model (Ex 2.7)

[x] Create RecipeSearchForm (Ex 2.7)

[x] Implement recipe_search view with filtering (Ex 2.7)

[x] Integrate data visualization charts (Ex 2.7)

[x] Write tests for search form and view (Ex 2.7)

[ ] To Do (Ex 2.8): Configure for deployment (settings, static files).

[ ] To Do (Ex 2.8): Deploy application to a PaaS (e.g., Render).

[ ] Implement recipe creation/editing via forms (Future Exercise).

Future Enhancements
(Unchanged)

Resources
(Unchanged)

Deliverables
{/* */}

Completed Django project source code for Exercises 2.1 - 2.7.

Functional search page with filtering and dynamic chart generation.

Passing unit tests for models, URLs, forms, and views.

Updated README.md and LEARNING_JOURNAL entries.

Required screenshots documenting functionality and testing.

Technical Notes
{/* */}

pandas and matplotlib added to requirements.txt.

Matplotlib uses 'Agg' backend in views.py.

Charts embedded via base64 data URIs.

Ingredient search uses Q objects for OR logic.

Author & Links
(Unchanged)

AI Assistance Note
(Unchanged)

Screenshots List
(Required screenshots per exercise, stored in PYTHON-ACHIEVEMENT-2 repo)

Exercise 2.1: ...

Exercise 2.2: ...

Exercise 2.3: ...

Exercise 2.4: ...

Exercise 2.5: ...

Exercise 2.6: ... {/* */}

Exercise 2.7: Empty search form, search results table, bar chart, pie chart, line chart, passing tests (test recipes.tests).