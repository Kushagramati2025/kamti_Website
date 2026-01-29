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

## 📦 Data Management (Database Syncing)

Since the SQLite database (`db.sqlite3`) is **not** shared in Git (to avoid conflicts), we use **Fixtures** to share website content (Industries, Services, Banners, etc.) between developers.

### **Option 1: Setting up / Syncing (After `git pull`)**
Run this script to update your database with the latest changes from the team:
```powershell
.\backend\scripts\load_data.bat
```

### **Option 2: Saving Your Changes (Before `git push`)**
If you have changed any website content (Services, Text, etc.), run this script before you commit:
```powershell
.\backend\scripts\save_data.bat
git add .
git commit -m "Update content"
git push
```

### **Summary of Files**
*   `db.sqlite3`: **Local only**. Contains your personal test data. Do not commit.
*   `backend/core/fixtures/core_data.json`: **Shared**. The source of truth for website content.
*   `media/`: **Shared**. Contains images which are currently tracked in Git.
