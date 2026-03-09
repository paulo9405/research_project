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
- **Thank You Page:** http://127.0.0.1:8000/thanks/ (public access)
- **Results Dashboard:** http://127.0.0.1:8000/results/ (public access)
- **Admin Panel:** http://127.0.0.1:8000/admin/ (login required)

**Note:** The Results Dashboard is publicly accessible so anyone who completes the survey can view the aggregated statistics. Only the Admin Panel requires login credentials to access individual survey responses.

---

## Accessing the Results Dashboard

The Results Dashboard shows charts and statistics about survey responses. **This page is publicly accessible** - anyone can view the aggregated data.

Simply go to: http://127.0.0.1:8000/results/

You can also click the **"Results"** link in the navigation menu.

---

## Accessing the Admin Panel

The Admin Panel allows you to view, edit, and manage individual survey responses. **Only admin users can access this area.**

### How to Access:

1. Go to http://127.0.0.1:8000/admin/
2. Enter your admin credentials:
   - Username: `admin`
   - Password: `123`
3. You will have access to view and manage all survey responses

You can also click the **"Admin"** link in the navigation menu.

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
