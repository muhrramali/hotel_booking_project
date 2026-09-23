# Kutwal Dream Resort – Hotel Management System
## DBMS Lab Project | Django 4.2 + MySQL (XAMPP)

A real-world hotel booking and management system for **Kutwal Dream Resort** in Haramosh Valley, Gilgit-Baltistan, Pakistan.

---

## Features

### Public Website (Guest-Facing)
- Beautiful resort landing page with mountain/lake images
- Online room booking with meal plan & bed type selection
- Guest registration and login
- View personal booking history
- About Kutwal Valley, rooms showcase, facilities, contact

### Staff Management Portal
- Dashboard with live statistics
- Room, Guest, Staff CRUD
- Reservation workflow: Pending → Confirm → Check-In → Check-Out
- Payment recording and tracking
- Housekeeping task management
- Django Admin panel

---

## Tech Stack
- **Python Django 4.2**
- **MySQL** via XAMPP
- **Bootstrap 5** + Custom CSS
- Images from Unsplash (mountain resort theme) + PHP project assets

---

## Setup Instructions

### 1. Start XAMPP MySQL
Open XAMPP Control Panel → Start **MySQL**

### 2. Install packages
```bash
cd hotel_booking
pip install -r requirements.txt
```

### 3. Create database
```bash
python setup_database.py
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Load sample data
```bash
python manage.py load_sample_data
```

### 6. Run server
```bash
python manage.py runserver
```

### 7. Open in browser
| URL | Description |
|-----|-------------|
| http://127.0.0.1:8000/ | Public resort website |
| http://127.0.0.1:8000/staff-login/ | Staff management login |
| http://127.0.0.1:8000/manage/ | Staff dashboard |
| http://127.0.0.1:8000/admin/ | Django admin |

### Default Staff Login
- **Username:** `admin`
- **Password:** `admin123`

---

## Database Tables
| Table | Purpose |
|-------|---------|
| Room | Resort rooms & chalets |
| Guest | Registered guests |
| Staff | Resort employees |
| Reservation | Bookings with status workflow |
| Payment | Payment records |
| HousekeepingLog | Room cleaning tasks |

---

## Project Structure
```
hotel_booking/
├── hotel/              # Django app (models, views, forms)
├── templates/
│   ├── public/         # Guest-facing website
│   └── manage/         # Staff dashboard
├── static/
│   ├── css/            # Stylesheets
│   └── images/         # Resort photos
├── setup_database.py   # MySQL DB creator
└── manage.py
```
