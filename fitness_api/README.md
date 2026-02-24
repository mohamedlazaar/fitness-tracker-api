# Fitness Tracker API 🚀

A Django REST API for tracking fitness activities. Users can log workouts (running, cycling, swimming, walking), view their history, and get basic metrics.

# API DEPLOYED URL
https://mohamedlazaar360.pythonanywhere.com/

## Features (completed)
- ✅ User authentication (register, login, profile)
- ✅ CRUD for fitness activities
- ✅ Users only see their own activities
- ✅ Activity filters (type, date range) and sorting
- ✅ Summary metrics endpoint

## Tech Stack
- Django 6.x / Django REST Framework
- SQLite (dev)
- DRF browsable API

## Quick Start

1. **Clone & setup:**
   ```bash
   git clone https://github.com/mohamedlazaar/fitness-tracker-api.git
   cd fitness-tracker-api/fitness_api
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Migrations & run server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. **Test in browser:**  
   - Login: http://127.0.0.1:8000/api-auth/  
   - Activities: http://127.0.0.1:8000/api/activities/

---

## Endpoints

Base URL: `http://127.0.0.1:8000`. Authenticated endpoints require login first; use session cookie (`-b cookies.txt` with curl).

### User Endpoints

1. **Register User**
   - *POST* `/api/users/register/`
   - *Request Body:*
   ```json
   {
     "username": "demo",
     "email": "demo@example.com",
     "password": "demopass123"
   }
   ```
   - *Response:* Created user (username, email). No password in response.

2. **Login User**
   - *POST* `/api/users/login/`
   - *Request Body:*
   ```json
   {
     "username": "demo",
     "password": "demopass123"
   }
   ```
   - *Response:* Session cookie for authentication; returns current user profile (id, username, email, first_name, last_name).

3. **User Details** (current user)
   - *GET* `/api/users/me/`
   - *Response:* Current user profile (id, username, email, first_name, last_name). Requires authentication.

4. **Update User** (profile)
   - *PATCH* `/api/users/me/`
   - *Request Body:*
   ```json
   {
     "first_name": "Demo",
     "last_name": "User",
     "email": "newemail@example.com"
   }
   ```
   - *Response:* Updated user profile. Requires authentication.

5. **Delete Account**
   - *DELETE* `/api/users/me/`
   - *Response:* 204 No Content. Requires authentication.

---

### Activity Endpoints

1. **List Activities**
   - *GET* `/api/activities/`
   - Supports filters: *activity_type* (running, cycling, swimming, walking, other), *start_date*, *end_date* (YYYY-MM-DD). Sorting: *ordering* (e.g. `-date`, `duration_minutes`, `-calories_burned`).
   - *Response:* Paginated list of the current user's activities. Requires authentication.

2. **Create Activity**
   - *POST* `/api/activities/`
   - *Request Body:*
   ```json
   {
     "activity_type": "running",
     "duration_minutes": 30,
     "distance_km": 5.2,
     "calories_burned": 280,
     "date": "2026-02-20"
   }
   ```
   - *Response:* Created activity (id, user, activity_type, duration_minutes, distance_km, calories_burned, date). Requires authentication.

3. **Activity Details**
   - *GET* `/api/activities/{id}/`
   - *Response:* Single activity by id. Requires authentication; user can only access own activities.

4. **Update Activity**
   - *PUT* `/api/activities/{id}/` (full update) or *PATCH* `/api/activities/{id}/` (partial update)
   - *Request Body (example for PATCH):*
   ```json
   {
     "duration_minutes": 35
   }
   ```
   - *Response:* Updated activity. Requires authentication.

5. **Delete Activity**
   - *DELETE* `/api/activities/{id}/`
   - *Response:* 204 No Content. Requires authentication.

6. **Activity Summary**
   - *GET* `/api/activities/summary/`
   - Optional query params: *start_date*, *end_date* (YYYY-MM-DD) to limit the period.
   - *Response:* Totals: total_activities, total_duration_minutes, total_distance_km, total_calories_burned. Requires authentication.

---


Run **Login** first and use `-b cookies.txt` for authenticated requests.

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/users/register/ -H "Content-Type: application/json" -d '{"username":"demo","email":"demo@example.com","password":"demopass123"}'

# Login (saves session to cookies.txt)
curl -X POST http://127.0.0.1:8000/api/users/login/ -H "Content-Type: application/json" -d '{"username":"demo","password":"demopass123"}' -c cookies.txt

# User details
curl -X GET http://127.0.0.1:8000/api/users/me/ -b cookies.txt

# Update profile
curl -X PATCH http://127.0.0.1:8000/api/users/me/ -H "Content-Type: application/json" -d '{"first_name":"Demo","last_name":"User"}' -b cookies.txt

# List activities
curl -X GET http://127.0.0.1:8000/api/activities/ -b cookies.txt

# List with filters
curl -X GET "http://127.0.0.1:8000/api/activities/?activity_type=running&start_date=2026-01-01&end_date=2026-12-31" -b cookies.txt

# Create activity
curl -X POST http://127.0.0.1:8000/api/activities/ -H "Content-Type: application/json" -d '{"activity_type":"running","duration_minutes":30,"distance_km":5.2,"calories_burned":280,"date":"2026-02-20"}' -b cookies.txt

# Get one activity (replace 1 with real id)
curl -X GET http://127.0.0.1:8000/api/activities/1/ -b cookies.txt

# Update activity
curl -X PATCH http://127.0.0.1:8000/api/activities/1/ -H "Content-Type: application/json" -d '{"duration_minutes":35}' -b cookies.txt

# Delete activity
curl -X DELETE http://127.0.0.1:8000/api/activities/1/ -b cookies.txt

# Summary
curl -X GET http://127.0.0.1:8000/api/activities/summary/ -b cookies.txt
```

---

## Project Status
ALX Backend Capstone – Fitness Tracker API ✅



## Repo structure

```
fitness-tracker-api/
├── fitness_api/          # Django project (manage.py here)
│   ├── fitness_api/      # settings, urls, wsgi
│   ├── activities/       # Activity CRUD, filters, summary
│   ├── users/            # Register, login, profile
│   └── manage.py
├── requirements.txt
└── README.md
```
