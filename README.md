# Recipe App – Django Web Application

_Achievement 2 • CareerFoundry – Python for Web Developers_

**Student:** Ivan Cortes  
**Repository:** `recipe-app` (Django-based Recipe Management System)  
**Last Updated:** October 17, 2025

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
This Django web application evolves the command‑line Recipe App from **Achievement 1** into a full web application following Django’s **MVT** (Model–View–Template) architecture. It adds authentication, protected views, image uploads, and model relationships, and includes example apps for a simple bookstore/sales domain to practice multi‑app projects.

**Current scope (Exercise 2.6):**
- Project with multiple Django apps
- Recipe management (with Ingredients via Many‑to‑Many through model)
- Image uploads for recipes (media handling)
- Styled pages for recipe list/detail
- **New:** User authentication (login/logout) and protected recipe views
- Example domain: Books, Customers, Salespersons, Sales
- SQLite database, migrations, and configured Django Admin
- URL and model tests

---

## Learning Objectives
By the end of Achievement 2 you will be able to:
- Explain and implement Django’s **MVT** pattern.
- Design models with **ForeignKey** and **Many‑to‑Many** (including `through`) relationships.
- Configure static/media files and handle **image uploads**.
- Build **Function‑Based Views (FBV)** and **Class‑Based Views (CBV)** (ListView, DetailView).
- Implement **authentication** (login/logout) and protect views with `LoginRequiredMixin`.
- Use **URL routing** with namespacing and reverse resolution (`{% url %}`, `redirect()`).
- Write and run **model/URL tests** using Django’s `TestCase`.

---

## Environment & Specs
- **Recommended (per course):** Python **3.9.x** (use a virtualenv)
- **Local dev used here:** Python **3.13.5**, Django **5.2.7** *(project runs on this stack; if following course specs, pin to Python 3.9 and a compatible Django per your tutor’s guidance)*
- **Database:** SQLite (development)
- **IDE:** VS Code (recommended)
- **Version Control:** Git + GitHub

> If you’re following CareerFoundry’s exact environment guidance, prefer Python **3.9** in a virtual environment.

---

## Project Structure
```
recipe-app/
├── recipe_project/          # Main project
│   ├── settings.py
│   ├── urls.py
│   └── views.py             # Project-level auth views (login/logout)
│
├── recipes/                 # Recipe management app
│   ├── migrations/
│   ├── templates/recipes/
│   │   ├── recipes_list.html
│   │   └── recipes_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py             # Uses LoginRequiredMixin
│
├── sales/                   # App for homepage
│   ├── templates/sales/
│   │   └── recipes_home.html  # Conditional login/view button
│   ├── urls.py
│   └── views.py
│
├── templates/               # Project-level templates
│   └── auth/
│       ├── login.html
│       └── logout_success.html
│
├── media/                   # User-uploaded images
│
├── books/                   # Example app
├── customers/               # Example app
├── salespersons/            # Example app
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── .gitignore
```

---

## Installation & Setup (Windows + Git Bash)

### 1) Clone the repository
```bash
git clone https://github.com/ivencomur/recipe-app.git
cd recipe-app
```

> **Tip:** If your local repo was created elsewhere and you need to push to `recipe-app`, add it as a remote:
```bash
git remote add origin https://github.com/ivencomur/recipe-app.git
# or if you already have an 'origin', add a second remote name:
# git remote add recipe-app https://github.com/ivencomur/recipe-app.git
```

### 2) Create & activate a virtual environment
**Course‑preferred (Python 3.9):**
```bash
python3 -m venv .venv   # or: python -m venv .venv
source .venv/Scripts/activate
```
> If `python3` is not found, use `py -3.9 -m venv .venv` then `source .venv/Scripts/activate`.

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Apply migrations
```bash
python manage.py migrate
```

### 5) Create a superuser (for Admin)
```bash
python manage.py createsuperuser
```

### 6) Run the development server
```bash
python manage.py runserver
```
Visit:
- App home: <http://127.0.0.1:8000/>
- Admin: <http://127.0.0.1:8000/admin/>

---

## Running the App
- Home page is served by the **sales** app’s view/template.
- Recipes list/detail require login. Use the top‑right link to **Log in**.
- Uploaded recipe images are saved under `media/` (ensure `MEDIA_URL`/`MEDIA_ROOT` configured in `settings.py`).

---

## Authentication & Access Control
- Project‑level `login`/`logout` views and templates under `templates/auth/`.
- `LoginRequiredMixin` protects recipe list/detail views.
- `LOGIN_URL` is set so unauthenticated users are redirected to login.
- Templates use `user.is_authenticated` to render login/logout buttons conditionally.

---

## Data Models
### Recipe Domain
**Recipe**
- `name` *(CharField)*
- `description` *(TextField)*
- `cook_time_minutes` *(PositiveIntegerField)*
- `pic` *(ImageField)*
- `ingredients` *(ManyToManyField through `RecipeIngredient`)*
- `created_at` *(DateTimeField auto‑added)*

**Ingredient**
- `name` *(CharField, unique)*

**RecipeIngredient** (through model)
- `recipe` *(ForeignKey → Recipe)*
- `ingredient` *(ForeignKey → Ingredient)*
- `quantity` *(FloatField)*
- `unit` *(CharField)*

### Book / Sales Examples
**Book**
- `name`, `author_name`, `price` *(Float)*, `genre` *(choices)*, `book_type` *(choices)*

**Customer**
- `name`, `notes`

**Salesperson**
- `username`, `name`, `bio`

---

## Testing
Run all tests:
```bash
python manage.py test
```
Specific app:
```bash
python manage.py test recipes
```
**Coverage focus:**
- Field validations & constraints (incl. `max_length`, validators, unique)
- Model string representations
- Default values
- M2M relationships via `RecipeIngredient`
- `get_absolute_url()` correctness

---

## Development Workflow
1. Create a feature branch from `main`.
2. Make changes and run locally.
3. Run tests (`python manage.py test`).
4. Commit with descriptive messages.
5. Push and open a Pull Request.

---

## Known Issues & TODOs
- [x] Implement recipe list/detail views
- [x] Create HTML templates for UI
- [x] Add URL routing for all apps
- [x] Implement recipe image uploads
- [x] Add User Authentication (Login/Logout)
- [x] Protect Recipe Views
- [ ] Implement recipe **search**
- [ ] Create **forms** for recipe creation/editing

---

## Future Enhancements
- Recipe categories and tags
- User favorites and ratings
- Shopping list generation
- Meal planning features
- Nutrition information

---

## Resources
**Documentation**
- Django Official Docs
- Django Tutorial
- Django Models Reference
- Django Admin Docs

**Course Materials**
- CareerFoundry – Python for Web Developers (Achievement 2)
- Exercise materials & course repo

---

## Deliverables
- Django project with multi‑app structure
- Protected recipe list & detail pages
- Working image upload pipeline
- Admin configured for all models
- Passing tests for models/URLs

---

## Technical Notes
- If you need to target the **`recipe-app`** GitHub repo explicitly from a different local folder, add or switch remotes:
  ```bash
  git remote -v
  git remote add recipe-app https://github.com/ivencomur/recipe-app.git
  # or switch your existing origin
  git remote set-url origin https://github.com/ivencomur/recipe-app.git
  ```
- Media files require proper `MEDIA_URL` and `MEDIA_ROOT` plus development `urlpatterns` to serve media in `DEBUG=True`.
- For strict course parity, prefer **Python 3.9** and lock Django to the version used in the module; otherwise ensure your installed Django supports your Python runtime (this project also runs on Python 3.13.5 + Django 5.2.7 locally).

---

## Author & Links
**Author:** Ivan Cortes

- **Portfolio:** ivan-cortes-portfolio-v1.onrender.com  
- **LinkedIn:** Ivan Cortes Murcia  
- **GitHub:** @ivencomur  
- **Twitter:** @IVENCOMUR

> This is a learning project for CareerFoundry’s Python course; feedback and suggestions are welcome!

---

## AI Assistance Note
Parts of this README and boilerplate scaffolding were organized with the help of an AI assistant for clarity, structure, and consistency. All code and configuration were reviewed and tested locally by the student.

---

## Screenshots List
Screenshots live in **PYTHON-ACHIEVEMENT-2** (separate repo). For Exercise **2.6**, include (suggested filenames):
1. `2.6_login_page.png` – Project‑level login screen
2. `2.6_recipes_list_protected.png` – Protected recipe list view (post‑login)
3. `2.6_recipe_detail_protected.png` – Protected recipe detail view (post‑login)
4. `2.6_logout_confirmation.png` – Logout confirmation page

