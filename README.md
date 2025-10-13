# Recipe App - Django Web Application

## 📚 Python for Web Developers - Achievement 2

**Student:** Ivan Cortes  
**Course:** CareerFoundry - Python for Web Developers  
**Repository:** Django-based Recipe Management System

---

## 🎯 Project Overview

This Django web application is the evolution of the command-line Recipe App from Achievement 1. It demonstrates the transition from CLI to web-based application using Django's MVT architecture.

### Current Features (Exercise 2.2)
- ✅ Django project structure with multiple apps
- ✅ Recipe management with ingredients (Many-to-Many relationships)
- ✅ Book inventory system (from bookstore example)
- ✅ Sales tracking with customers and salespersons
- ✅ SQLite database with migrations
- ✅ Django admin interface configured
- ✅ Comprehensive model testing

---

## 📁 Project Structure

```
recipe_project/
├── recipe_project/          # Main Django project folder
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI config for production
│   └── asgi.py            # ASGI config for async
│
├── recipes/                # Recipe management app
│   ├── models.py          # Recipe, Ingredient, RecipeIngredient models
│   ├── admin.py           # Admin interface configuration
│   ├── tests.py           # Model tests
│   ├── views.py           # Views (to be implemented)
│   └── migrations/        # Database migrations
│
├── books/                  # Book inventory app
│   ├── models.py          # Book model with genres and types
│   ├── admin.py           # Book admin configuration
│   ├── tests.py           # Book model tests
│   └── migrations/
│
├── sales/                  # Sales tracking app
│   ├── models.py          # Sale model (to be implemented)
│   ├── admin.py
│   └── migrations/
│
├── customers/              # Customer management app
│   ├── models.py          # Customer model
│   ├── admin.py
│   └── migrations/
│
├── salespersons/          # Salesperson management app
│   ├── models.py          # Salesperson model
│   ├── admin.py
│   └── migrations/
│
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database
├── requirements.txt      # Python dependencies
└── .gitignore           # Git ignore file
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/ivencomur/recipe-app.git
cd recipe-app
```

### Step 2: Create Virtual Environment
```bash
# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install Django==5.2.7
# Or use requirements.txt if available
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (for Admin Access)
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/admin

---

## 📊 Data Models

### Recipe App Models

#### Recipe Model
- **name**: CharField (recipe name)
- **description**: TextField (recipe instructions)
- **cook_time_minutes**: PositiveIntegerField (cooking time)
- **ingredients**: ManyToManyField (through RecipeIngredient)
- **created_at**: DateTimeField (auto-added)

#### Ingredient Model
- **name**: CharField (unique ingredient name)

#### RecipeIngredient Model (Junction Table)
- **recipe**: ForeignKey to Recipe
- **ingredient**: ForeignKey to Ingredient
- **quantity**: FloatField (amount needed)
- **unit**: CharField (measurement unit)

### Book Inventory Models

#### Book Model
- **name**: CharField
- **author_name**: CharField
- **price**: FloatField (in USD)
- **genre**: CharField with choices (Classic, Romantic, Comic, Fantasy, Horror, Educational)
- **book_type**: CharField with choices (Hardcover, E-Book, Audiobook)

### Customer & Sales Models
- **Customer**: name and notes
- **Salesperson**: username, name, and bio

---

## 🧪 Running Tests

### Run All Tests
```bash
python manage.py test
```

### Run Tests for Specific App
```bash
python manage.py test recipes
python manage.py test books
```

### Test Coverage
- ✅ Model field validations
- ✅ Model string representations
- ✅ Default values
- ✅ Field constraints (max_length, validators)
- ✅ Unique constraints
- ✅ Many-to-Many relationships

---

## 🎓 Learning Journey

### Exercise 2.1 - Getting Started with Django
- Researched Django's popularity and use cases
- Set up development environment with virtual environment
- Installed Django and verified installation
- Learned MVT architecture vs MVC

### Exercise 2.2 - Django Project Structure (Current)
- Created Django project with `django-admin startproject`
- Created multiple apps using `python manage.py startapp`
- Designed database models with relationships
- Configured Django admin interface
- Wrote model tests for validation
- Understood Django's file organization

### Upcoming Exercises
- **Exercise 2.3**: Views and Templates
- **Exercise 2.4**: Django URLs and Forms
- **Exercise 2.5**: Django Testing
- **Exercise 2.6**: User Authentication
- **Exercise 2.7**: Data Analysis and Visualization
- **Exercise 2.8**: Deployment

---

## 💡 Key Django Concepts Applied

### MVT Architecture
- **Models**: Database structure (recipes, ingredients, books)
- **Views**: Business logic (to be implemented)
- **Templates**: HTML presentation (to be implemented)

### Django ORM
- Model definitions with field types
- Model relationships (ForeignKey, ManyToMany)
- Migrations for database schema changes
- QuerySets for database queries

### Django Admin
- Automatic admin interface generation
- Model registration with customization
- List display, search, and filters
- Inline editing for related models

---

## 🐛 Known Issues & TODOs

### Current TODOs
- [ ] Implement views for recipe listing and details
- [ ] Create HTML templates for user interface
- [ ] Add URL routing for all apps
- [ ] Implement recipe search functionality
- [ ] Add recipe difficulty calculation
- [ ] Create forms for recipe creation/editing
- [ ] Add user authentication
- [ ] Implement recipe image uploads

### Future Enhancements
- Recipe categories and tags
- User favorites and ratings
- Shopping list generation
- Meal planning features
- Nutrition information
- Recipe sharing functionality

---

## 📚 Resources

### Documentation
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
- [Django Models Reference](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Admin Documentation](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

### Course Materials
- CareerFoundry Python for Web Developers
- Achievement 2 Exercise Materials
- [Course Repository](https://github.com/ivencomur/PYTHON-ACHIEVEMENT-2)

---

## 🤝 Contributing

This is a learning project for CareerFoundry's Python course. While it's primarily for educational purposes, feedback and suggestions are welcome!

### Development Workflow
1. Create feature branch from main
2. Make changes and test locally
3. Run tests to ensure nothing breaks
4. Commit with descriptive messages
5. Push and create pull request

---

## 📝 License

This project is part of CareerFoundry's educational curriculum and is for learning purposes.

---

## 👤 Author

**Ivan Cortes**
- Portfolio: [ivan-cortes-portfolio-v1.onrender.com](https://ivan-cortes-portfolio-v1.onrender.com/)
- LinkedIn: [Ivan Cortes Murcia](https://www.linkedin.com/in/ivan-cortes-murcia-22053953/)
- GitHub: [@ivencomur](https://github.com/ivencomur)
- Twitter: [@IVENCOMUR](https://x.com/IVENCOMUR)

---

## 🙏 Acknowledgments

- CareerFoundry for the comprehensive curriculum
- Django Software Foundation for the excellent framework
- Python community for extensive documentation and support

---

## 📸 Screenshots

### Django Admin Interface
*Coming soon: Screenshots of the admin interface showing recipe and book management*

### Project Structure in VS Code
*Coming soon: IDE view showing the organized project structure*

### Test Results
*Coming soon: Terminal output showing successful test runs*

---

## 🔧 Technical Stack

- **Language**: Python 3.13.5
- **Framework**: Django 5.2.7
- **Database**: SQLite (development)
- **Version Control**: Git/GitHub
- **IDE**: VS Code
- **Testing**: Django's built-in TestCase

---

*Last Updated: October 2025*
*Course: CareerFoundry - Python for Web Developers*
*Achievement 2 - Web Development with Django*