# Step-by-Step Testing Guide

This guide explains what was built and how to run and test everything on your local machine.

---

## What Was Built

| File | What it does |
|------|--------------|
| `survey/models.py` | Database table that stores each survey response |
| `survey/views.py` | Logic for the 3 pages (form, thank you, results) |
| `survey/urls.py` | URL routes: `/`, `/thanks/`, `/results/` |
| `survey/admin.py` | Registers the survey data in Django Admin |
| `templates/survey/survey_form.html` | Survey form page |
| `templates/survey/thanks.html` | Thank you confirmation page |
| `templates/survey/results.html` | Results dashboard with charts |

---

## Step 1 — Get the Latest Code

Open your terminal, go to the project folder and pull the latest changes:

```bash
cd ~/projects/research_project
git checkout your-branch-name
git pull origin main
```

> Replace `your-branch-name` with your branch (e.g. `lucas`, `larissa`, etc.)

---

## Step 2 — Activate the Virtual Environment

**Linux / Mac:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

You should see `(venv)` at the start of your terminal line.

---

## Step 3 — Install Dependencies

Only needed if you haven't done this before, or if `requirements.txt` changed:

```bash
pip install -r requirements.txt
```

---

## Step 4 — Run the Database Migrations

This creates the survey table in the database:

```bash
python manage.py migrate
```

Expected output includes a line like:
```
Applying survey.0001_initial... OK
```

---

## Step 5 — Create an Admin User

You need this to access the Admin panel and the Results page:

```bash
python manage.py createsuperuser
```

Fill in:
- **Username:** choose any (e.g. your name)
- **Email:** can be left blank (just press Enter)
- **Password:** choose any password (minimum 8 characters)

---

## Step 6 — Start the Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

---

## Step 7 — Test the Application

Open your browser and test each page:

### Page 1 — Survey Form
```
http://127.0.0.1:8000/
```
- Select one of the reason cards (Learn English, Job Opportunities, etc.)
- If you select **Other**, a text field should appear
- Fill in all personal information fields
- Click **Submit Survey**
- You should be redirected to the Thank You page

---

### Page 2 — Thank You Page
```
http://127.0.0.1:8000/thanks/
```
- Should show a green checkmark and a thank you message
- Click **Explore the Results** — it will ask you to log in

---

### Page 3 — Results Dashboard (login required)
```
http://127.0.0.1:8000/results/
```
- You will be redirected to the login page automatically
- Log in with the superuser you created in Step 5
- After login you should see:
  - Total number of responses
  - Bar chart with reasons
  - Doughnut chart with age groups

---

### Admin Panel
```
http://127.0.0.1:8000/admin/
```
- Log in with your superuser credentials
- Click on **Survey responses**
- You should see all submitted responses listed
- You can click any entry to view or edit the details
- Use the **Reason** filter on the right sidebar to filter by option

---

## Quick Summary — Commands to Run Every Time

```bash
cd ~/projects/research_project
git checkout your-branch-name
git pull origin main
source venv/bin/activate
python manage.py migrate
python manage.py runserver
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `No module named django` | Run `source venv/bin/activate` first |
| `Table not found` error | Run `python manage.py migrate` |
| Results page shows login form | That is correct — log in with your superuser |
| Port 8000 already in use | Use `python manage.py runserver 8001` |
| `python: command not found` | Use `python3` instead of `python` |

---

**Questions? Contact Paulo (team leader).**
