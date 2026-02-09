# Backend - KMATI Website

This is the Django REST Framework backend for the KMATI website.

## Prerequisites
- **Python**: v3.10+
- **Virtual Environment** (Recommended)

## 🚀 Setup & Installation

### 1. Create Virtual Environment
```bash
# Windows
python -m venv venv

# Mac/Linux
python3 -m venv venv
```

### 2. Activate Virtual Environment
```bash
# Windows
.\venv\Scripts\Activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Since the database (`db.sqlite3`) is ignored in Git, you must create it locally.

```bash
# Run migrations to create tables
python manage.py migrate
```

### 5. Populate Initial Content
Run the following scripts to fill the database with initial data (Services, Industries, Text, etc.):

```bash
# Populate main content
python scripts/populate_real_content.py

# Optional: Fetch images
python scripts/fetch_images.py
```

## 🏃 Running the Server

```bash
python manage.py runserver 0.0.0.0:8000
```
The API will be available at: http://127.0.0.1:8000

## 🔧 Common Commands

| Task | Command |
|------|---------|
| **Create Superuser** | `python manage.py createsuperuser` |
| **Make Migrations** | `python manage.py makemigrations` |
| **Apply Migrations** | `python manage.py migrate` |

## 📦 Data Management (Fixtures)
We use fixtures to share core website content since the DB is local.

- **Load Data** (After git pull):
  `.\scripts\load_data.bat`
  
- **Save Data** (Before git push):
  `.\scripts\save_data.bat`


### ⚠️ Troubleshooting: Encoding Issues
If `load_data.bat` fails with a `UnicodeDecodeError` (often caused by Windows encoding), you can manually fix the fixture file:

```bash
# Verify and fix encoding of core_data.json
python scripts/fix_encoding.py
```
Then try loading the data again.
