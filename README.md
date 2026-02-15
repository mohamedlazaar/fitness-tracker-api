# Fitness Tracker API 🚀

A Django REST API for tracking fitness activities. Users can log workouts (running, cycling, gym), view their history, and get basic metrics.

## Features (completed)
- ✅ User authentication  
- ✅ CRUD for fitness activities  
- ✅ Users only see their own activities  
- ✅ RESTful API endpoints at `/api/activities/`

## Tech Stack
- Django 5.x  
- Django REST Framework  
- SQLite (dev), PostgreSQL (prod)  
- DRF browsable API  

## Quick Start

1. **Clone & setup:**
   ```bash
   git clone https://github.com/mohamedlazaar/fitness-tracker-api.git
   cd fitness-tracker-api
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
Run migrations & create superuser:


python manage.py migrate
python manage.py createsuperuser
Start server:


python manage.py runserver
Test API:

Login: http://127.0.0.1:8000/api-auth/

Activities: http://127.0.0.1:8000/api/

API Endpoints
text
POST /api/activities/    # Create activity
GET  /api/activities/    # List user's activities
GET  /api/activities/1/  # Single activity
PUT  /api/activities/1/  # Update
DELETE /api/activities/1/ # Delete
Next Features (Week 4+)
Activity filtering (type, date range)

Pagination & sorting

Summary metrics endpoint

Deployment to PythonAnywhere

Project Status
Part 3 of ALX Backend Capstone ✅

Built during ALX Backend Capstone | [Your Name]



## 2. Your repo structure should look like this:
fitness-api/
├── fitness_api/ # main Django project
│ ├── init.py
│ ├── settings.py
│ ├── urls.py # ✅ has api/ and api-auth/
│ └── wsgi.py
├── activities/ # ✅ your app
│ ├── init.py
│ ├── models.py # ✅ Activity model
│ ├── serializers.py # ✅ ActivitySerializer
│ ├── views.py # ✅ ActivityViewSet
│ └── urls.py # ✅ DRF router
├── manage.py
├── requirements.txt # pip freeze > requirements.txt
├── README.md # ✅ paste above
└── .gitignore # python standard gitignore



## 3. Quick commands to finalize:
```bash
pip freeze > requirements.txt
git add .
git commit -m "Complete Part 3 setup: models, views, URLs, README"
git push origin main
