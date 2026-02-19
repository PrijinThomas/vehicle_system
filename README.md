# 🚗 Vehicle Inventory & Booking REST API

A Django REST Framework backend project that allows users to manage vehicles and create bookings with real-world business validations.

This project demonstrates backend development skills including API structuring, validation logic, filtering, and database management.

---

## 📌 Features

### ✅ Vehicle Management
- Add new vehicles
- View all vehicles
- View vehicle details
- Update vehicle details
- Delete vehicles
- Filter vehicles by:
  - Brand
  - Fuel type
  - Availability

### ✅ Booking System
- Create bookings for vehicles
- Prevent overlapping bookings
- Automatically calculate total booking amount
- Validate phone number (10 digits only)
- Ensure start date is not in the past
- Ensure end date is after start date
- Automatically mark vehicle unavailable after booking

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (Development Database)
- PostgreSQL (Production Ready)

---

## 📂 Project Structure

vehicle_system/
│
├── inventory/ # App folder
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│
├── vehicle_system/ # Project settings
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .env.example


---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd vehicle_system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

Activate it:

**Windows:**
```bash
env\Scripts\activate
```

**Mac/Linux:**
```bash
source env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```



📡 API Endpoints
🚗 Vehicle Endpoints

Method	    Endpoint	        Description
GET	        /api/vehicles/	    List all vehicles
POST	    /api/vehicles/	    Add a vehicle
GET	        /api/vehicles/<id>/	Get vehicle details
PUT	        /api/vehicles/<id>/	Update vehicle
DELETE	    /api/vehicles/<id>/	Delete vehicle

📅 Booking Endpoints

Method	    Endpoint	        Description
GET	        /api/bookings/	    List all bookings
POST	    /api/bookings/	    Create booking
GET	        /api/bookings/<id>/	Get booking details


🔍 Filtering Support

You can filter vehicles using query parameters:

/api/vehicles/?brand=Toyota
/api/vehicles/?fuel_type=Electric
/api/vehicles/?is_available=true


📦 Sample Booking JSON

Use this when creating a booking:

```bash

{
  "vehicle": 1,
  "customer_name": "Rahul Sharma",
  "customer_phone": "9876543210",
  "start_date": "2026-03-10",
  "end_date": "2026-03-15"
}


```

🧠 Business Logic Implemented

Vehicle cannot be double-booked
Overlapping booking dates are prevented
total_amount = number_of_days × price_per_day
Phone number must be exactly 10 digits
Start date cannot be in the past
End date must be after start date
Vehicle becomes unavailable after booking



🧪 API Testing

APIs can be tested using:

Postman
Django REST Framework Browsable API

☁ Deployment

This project is deployed on the platforms:
Render


👨‍💻 Author

Developed as part of a Django Backend Evaluation Task.