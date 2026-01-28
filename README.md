# KMATI Website Project

## Prerequisites
- **Node.js**: v18+ (Recommended v20 or latest)
- **Python**: v3.10+
- **Git**

## Project Structure
- `backend/`: Django REST Framework application
- `frontend/`: Angular application (v17+)

---

## 🚀 Quick Start Guide (New System Setup)

Follow these steps to set up the project on a new machine after pulling the code.

### 1. Backend Setup (Django)

Open a terminal in the root folder (`d:\kmati_website`).

1.  **Create Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    
    # Mac/Linux
    python3 -m venv venv
    ```

2.  **Activate Virtual Environment**
    ```bash
    # Windows
    .\venv\Scripts\Activate
    
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Database Setup (Important!)**
    Since the database (`db.sqlite3`) is not committed to Git, you must create it locally.
    ```bash
    cd backend
    python manage.py migrate
    ```

5.  **Populate Initial Data**
    Run the content script to fill the empty database with services, industries, and text.
    ```bash
    python populate_real_content.py
    # Optional: fetch images if they are missing
    python fetch_images.py
    ```

6.  **Run Server**
    ```bash
    python manage.py runserver
    ```
    *Backend will be available at: http://127.0.0.1:8000*

---

### 2. Frontend Setup (Angular)

Open a **new** terminal (keep the backend running) and navigate to the frontend folder.

1.  **Navigate to Folder**
    ```bash
    cd frontend
    ```

2.  **Install Dependencies**
    ```bash
    npm install
    ```

3.  **Run Development Server**
    ```bash
    npm start
    # or
    ng serve
    ```
    *Frontend will be available at: http://localhost:4200*

---

## 🔧 Common Commands

| Task | Command |
|------|---------|
| **create user** | `python manage.py createsuperuser` |
| **make migrations** | `python manage.py makemigrations` |
| **apply migrations** | `python manage.py migrate` |
| **frontend build** | `ng build` |
