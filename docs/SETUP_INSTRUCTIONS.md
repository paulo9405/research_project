# Setup Instructions for Team Members

This guide will help you set up the Django project after pulling the latest changes from `main`.

---

## Prerequisites

Make sure you have installed:

- **Python 3.10+** (check with `python3 --version`)
- **pip** (check with `pip --version`)

---

## Step-by-Step Setup

### Step 1: Open Terminal and Navigate to Project

```bash
cd ~/projects/research_project
```

**What this does:** Opens the project folder in your terminal.

---

### Step 2: Switch to Your Branch

```bash
git checkout your-branch-name
```

**Example for Lucas:**
```bash
git checkout lucas
```

**What this does:** Makes sure you are on your personal branch.

---

### Step 3: Pull the Latest Changes from Main

```bash
git pull origin main
```

**What this does:** Downloads all the new files Paulo added to the `main` branch (Django project, templates, settings, etc.) and merges them into your branch.

---

### Step 4: Create a Virtual Environment

```bash
python3 -m venv venv
```

**What this does:** Creates a folder called `venv` with an isolated Python environment. This keeps project dependencies separate from your system.

---

### Step 5: Activate the Virtual Environment

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**What this does:** Activates the virtual environment. You will see `(venv)` at the start of your terminal line.

---

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

**What this does:** Installs Django and all required packages listed in `requirements.txt`.

---

### Step 7: Run Database Migrations

```bash
python manage.py migrate
```

**What this does:** Creates the database file (`db.sqlite3`) and sets up all necessary tables.

---

### Step 8: Create a Superuser

```bash
python manage.py createsuperuser
```

**What this does:** Creates an admin account so you can access `/admin/` and view the results dashboard.

**Default credentials for testing:**
- **Username:** admin
- **Password:** 123

**Important:** Each team member can create their own admin user if needed. You need admin access to view the Results Dashboard at `/results/`.

---

### Step 9: Run the Development Server

```bash
python manage.py runserver
```

**What this does:** Starts the local server at http://127.0.0.1:8000/

---

### Step 10: Test the Setup

Open your browser and test these pages:

- **Survey Form:** http://127.0.0.1:8000/ (public access)
- **Admin Panel:** http://127.0.0.1:8000/admin/ (login required)
- **Results Dashboard:** http://127.0.0.1:8000/results/ (admin login required)

**Note:** The Results Dashboard is only accessible to admin users. If you try to access it without logging in, you will see an "Access Restricted" page with a button to log in as admin.

---

## Accessing the Results Dashboard

The Results Dashboard shows charts and statistics about survey responses. **Only admin users can access this page.**

### How to Access:

1. Go to http://127.0.0.1:8000/results/
2. If not logged in, you'll see an "Access Restricted" page
3. Click the **"Admin Login"** button
4. Enter your admin credentials:
   - Username: `admin`
   - Password: `123`
5. After login, you will be redirected to the Results Dashboard

### Alternative Access:

You can also access the results from the navigation menu after logging in as admin.

---

## Quick Commands Summary

```bash
# Navigate to project
cd ~/projects/research_project

# Switch to your branch
git checkout your-branch-name

# Pull latest from main
git pull origin main

# Create virtual environment (only once)
python3 -m venv venv

# Activate virtual environment (every time)
source venv/bin/activate

# Install dependencies (only once, or when requirements.txt changes)
pip install -r requirements.txt

# Run migrations (when models change)
python manage.py migrate

# Start server
python manage.py runserver
```

---

## Daily Workflow

Every time you start working:

```bash
cd ~/projects/research_project
source venv/bin/activate
git pull origin main
python manage.py runserver
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python: command not found` | Use `python3` instead of `python` |
| `No module named django` | Activate venv: `source venv/bin/activate` |
| `Port 8000 already in use` | Use another port: `python manage.py runserver 8001` |

---

**Need help?** Contact Paulo (team leader).
