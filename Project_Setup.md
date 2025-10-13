# Recipe App - Project Setup Guide

## 📋 Complete File Structure

This document provides a complete guide to setting up the Recipe App Django project from the repository.

## 🏗️ Required Files

### Root Directory Files
- `manage.py` - Django management script
- `README.md` - Project documentation
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore file
- `index.html` - Learning journey documentation
- `LEARNING_JOURNAL_2.1.html` - Exercise 2.1 journal
- `LEARNING_JOURNAL_2.2.html` - Exercise 2.2 journal

### Project Configuration (recipe_project/)
- `__init__.py` - Package initializer
- `settings.py` - Django settings
- `urls.py` - URL configuration
- `wsgi.py` - WSGI configuration
- `asgi.py` - ASGI configuration

### Apps Structure

Each app should have these files:
- `__init__.py` - Package initializer
- `apps.py` - App configuration
- `models.py` - Database models
- `admin.py` - Admin interface
- `views.py` - View functions
- `tests.py` - Unit tests
- `migrations/` - Migration directory
  - `__init__.py` - Package initializer
  - Migration files (auto-generated)

## 📦 App-Specific Files

### recipes/
**models.py** - Contains Recipe, Ingredient, RecipeIngredient models  
**admin.py** - Admin configuration with inline editing  
**tests.py** - Comprehensive model tests

### books/
**models.py** - Book model with genre and type choices  
**admin.py** - Book admin with search and filters  
**tests.py** - Book model validation tests

### sales/
**models.py** - Sale model linking books, customers, salespersons  
**admin.py** - Sale admin with date hierarchy  
**tests.py** - Sale transaction tests

### customers/
**models.py** - Customer model with notes  
**admin.py** - Simple customer admin  
**tests.py** - Customer model tests

### salespersons/
**models.py** - Salesperson model with unique username  
**admin.py** - Salesperson admin with search  
**tests.py** - Salesperson validation tests

## 🚀 Setup Instructions

### 1. Clone and Navigate
```bash
git clone https://github.com/ivencomur/recipe-app.git
cd recipe-app
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
source venv/Scripts/activate  # Git Bash
# or
venv\Scripts\activate.bat  # Command Prompt

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# Install core dependencies only
pip install Django==5.2.7

# Or install all dependencies
pip install -r requirements.txt
```

### 4. Apply Missing Files
If any files are missing from the repository, copy them from the outputs:
- Copy all `sales_*.py` files to the `sales/` directory
- Copy all `customers_*.py` files to the `customers/` directory  
- Copy all `salespersons_*.py` files to the `salespersons/` directory

Rename the files appropriately:
- `sales_models.py` → `sales/models.py`
- `sales_admin.py` → `sales/admin.py`
- etc.

### 5. Create and Apply Migrations
```bash
# Create migration files for all apps
python manage.py makemigrations

# Apply migrations to create database tables
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
# Follow prompts to set username, email, and password
```

### 7. Run Tests
```bash
# Run all tests
python manage.py test

# Run tests for specific apps
python manage.py test recipes
python manage.py test books
python manage.py test sales
python manage.py test customers
python manage.py test salespersons
```

### 8. Start Development Server
```bash
python manage.py runserver
# Server starts at http://127.0.0.1:8000/
```

### 9. Access Admin Interface
1. Navigate to http://127.0.0.1:8000/admin
2. Login with superuser credentials
3. Start adding data through the admin interface

## 🧪 Testing the Setup

### Quick Verification Checklist
- [ ] Virtual environment activated
- [ ] Django installed (check with `pip show django`)
- [ ] All apps listed in INSTALLED_APPS
- [ ] Migrations applied successfully
- [ ] Admin interface accessible
- [ ] All models visible in admin
- [ ] Tests passing for all apps

### Sample Data Entry
1. **Add Ingredients**: flour, eggs, milk, sugar, salt
2. **Create Recipe**: Pancakes with ingredients
3. **Add Books**: Sample inventory items
4. **Create Customers**: Test customer profiles
5. **Add Salespersons**: Sales team members
6. **Record Sales**: Link books to customers

## 🐛 Common Issues and Solutions

### Issue: ModuleNotFoundError
**Solution**: Ensure virtual environment is activated and Django is installed

### Issue: No such table error
**Solution**: Run migrations: `python manage.py makemigrations && python manage.py migrate`

### Issue: Admin not showing models
**Solution**: Check that models are registered in admin.py and app is in INSTALLED_APPS

### Issue: Tests failing
**Solution**: Ensure test database permissions and check for migration conflicts

## 📚 Next Steps

### Exercise 2.3 - Views and Templates
- Create view functions for recipe listing
- Build HTML templates with Django template language
- Implement template inheritance
- Add CSS styling

### Exercise 2.4 - URLs and Forms
- Configure URL patterns
- Create forms for recipe input
- Implement CRUD operations
- Add form validation

### Exercise 2.5 and Beyond
- Comprehensive testing
- User authentication
- Data visualization
- Production deployment

## 📞 Support

If you encounter issues:
1. Check the learning journals for context
2. Review Django documentation
3. Verify all files are in correct locations
4. Ensure Python version compatibility (3.8+)
5. Check repository issues on GitHub

## ✅ Success Indicators

You know the setup is successful when:
- ✅ Server runs without errors
- ✅ Admin interface displays all 5 apps
- ✅ Models are editable in admin
- ✅ Tests pass for all apps
- ✅ Database file (db.sqlite3) is created
- ✅ You can create and save records

---

*Last Updated: October 2025*  
*Course: CareerFoundry - Python for Web Developers*  
*Repository: https://github.com/ivencomur/recipe-app*