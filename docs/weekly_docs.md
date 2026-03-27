# Weekly Documentation

This file documents the progress of the project each week.

---

## Week 1

**Date:** January 2025

### What we did

- Team meeting to define the project architecture and technologies
- Decided on a simple project with 3 screens related to surveys/research
- Created an empty repository on GitHub
- Each team member cloned the repository to their computer

### Technologies chosen

| Technology | Purpose |
|------------|---------|
| Python | Backend language |
| Django | Web framework |
| Bootstrap | Frontend styling |
| SQLite | Database (native with Django) |

### Why these choices

- **Django**: Easy to learn and has many built-in features
- **Bootstrap**: Fast way to make the app look good
- **SQLite**: Comes with Django, no extra setup needed

### Next steps

- Start building the project structure
- Create the first screens

---

## Week 2

**Date:** February 2026

### What we did

- Created the Django project (`ireland_survey`) and app (`survey`)
- Configured `settings.py` (allowed hosts, static files, templates directory)
- Added `.gitignore` for Python/Django
- Created `requirements.txt` with Django, gunicorn, and python-dotenv
- Built `base.html` template with Bootstrap 5, custom CSS variables, and Google Fonts (Inter)
- Built `navbar.html` with navigation links to Survey and Results
- Defined UI design guidelines (colors, typography, spacing, components)
- Added frontend reference screens to `front-end/` folder (form, thank you, dashboard)

### Next steps

- Implement the database model
- Build the 3 application screens

---

## Week 3

**Date:** February 2026

### What we did

**Backend:**
- Created `SurveyResponse` model with all fields: `reason`, `reason_other`, `full_name`, `age`, `email`, `nationality`, `city`, `created_at`
- Registered model in Django Admin with list display and sidebar filter
- Implemented 3 views: `survey_form`, `thanks`, `results` (results protected with `@login_required`)
- Created `survey/urls.py` with routes for `/`, `/thanks/`, `/results/`
- Connected survey URLs to the main `ireland_survey/urls.py`

**Frontend (Templates):**
- Built `survey_form.html` — option cards for each reason, personal info fields, JavaScript toggle for the "Other" text field
- Built `thanks.html` — confirmation page with checkmark icon and link to results
- Built `results.html` — dashboard with Chart.js bar chart (reasons) and doughnut chart (age groups), data fed from Django view context

**Documentation:**
- Added `step_by_step.md` with full instructions for team members to run and test the app locally

### Technologies added

| Technology | Purpose |
|------------|---------|
| Chart.js | Interactive charts on the results dashboard |
| Bootstrap Icons | Icons on form fields and buttons |

### Next steps

- Run `python manage.py migrate` to apply the database migration
- Each member creates a superuser with `python manage.py createsuperuser`
- Test all 3 screens locally (see `docs/step_by_step.md`)
- Build login page and configure Django authentication (Phase 5)
- Deploy to EasyPanel (Phase 7)

---
