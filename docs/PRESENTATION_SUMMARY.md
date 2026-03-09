# Ireland Survey Project - Presentation Summary

## Team Members
- **Larissa** - Frontend Development
- **Lucas** - Backend Development
- **Matheus** - Frontend Development
- **Paulo** - Technical Support

---

## 1. Project Overview

**Name:** Ireland Immigration Survey
**Goal:** A web application to collect and analyze data about why people choose to live in Ireland.

**Main Question:** *"Why did you choose to live in Ireland?"*

---

## 2. What We Built

### 2.1 Survey Form (Screen 1)
**URL:** `/`

- Main question with 5 options:
  - Learn English
  - Job Opportunities
  - Quality of Life
  - Career / Future
  - Other (with text field)

- Personal information fields:
  - Full Name
  - Age
  - Email
  - Nationality
  - Current City in Ireland

- **Features:**
  - "Other" text field appears only when selected (JavaScript)
  - Form validation (required fields, email format)
  - Mobile-friendly design with Bootstrap 5

### 2.2 Thank You Page (Screen 2)
**URL:** `/thanks/`

- Success message with checkmark icon
- Button to view results dashboard
- Same design style as other pages

### 2.3 Results Dashboard (Screen 3)
**URL:** `/results/`

- **Login required** (only logged-in users can see this page)
- Shows statistics:
  - Total number of responses
  - Bar chart: responses by reason
  - Doughnut chart: responses by age group (18-24, 25-34, 35+)
- Interactive charts using Chart.js

### 2.4 Admin Panel
**URL:** `/admin/`

- Django Admin access
- View all survey responses
- Filter by selected reason
- Edit or delete responses

---

## 3. Technical Structure

### 3.1 Backend
- **Framework:** Django 4.x
- **Language:** Python 3.x
- **Database:** SQLite

**Database Model (SurveyResponse):**
```
- reason (selected option)
- reason_other (extra text if "Other")
- full_name
- age
- email
- nationality
- city
- created_at (automatic timestamp)
```

### 3.2 Frontend
- **CSS Framework:** Bootstrap 5
- **Font:** Google Fonts (Inter)
- **Charts:** Chart.js (interactive)
- **Icons:** Bootstrap Icons
- Works on mobile and desktop

### 3.3 Project Structure
```
research_project/
├── ireland_survey/          # Django project settings
├── survey/                  # Main app
│   ├── models.py           # Database model
│   ├── views.py            # Page logic
│   ├── urls.py             # Routes
│   └── admin.py            # Admin configuration
├── templates/
│   ├── base.html           # Base template
│   ├── navbar.html         # Navigation bar
│   └── survey/
│       ├── survey_form.html
│       ├── thanks.html
│       └── results.html
├── docs/                   # Full documentation
└── requirements.txt        # Python packages
```

---

## 4. DevOps Practices

### 4.1 Version Control
- **Git/GitHub:** Central repository
- **Branch Strategy:**
  - `main` - protected branch (stable code)
  - Individual branches: `larissa`, `lucas`, `matheus`
  - Pull Requests to merge code

### 4.2 Collaboration
- Complete documentation in `docs/` folder
- Setup and testing guides
- Weekly progress tracking

### 4.3 Automation
- Automatic database migrations
- Built-in authentication system
- Automatic form validation

---

## 5. How to Test Locally

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Install packages
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create admin user (first time only)
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

**Test URLs:**
- Survey Form: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/
- Results: http://127.0.0.1:8000/results/

---

## 6. Current Status

### ✅ Completed
- Django project structure
- Database model working
- All 3 screens functional (form, thanks, results)
- Login system configured
- Dashboard with interactive charts
- Admin panel working
- Complete technical documentation
- Local testing successful

### 🔄 Next Steps
- Deploy to production server (EasyPanel)
- Collect real data using QR code
- Final documentation for CA2

---

## 7. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Backend language |
| Django 4.x | Web framework |
| SQLite | Database |
| Bootstrap 5 | CSS framework |
| Chart.js | Data visualization |
| Git/GitHub | Version control |
| Moodle | Assignment submission |

---

## 8. Project Metrics

- **Duration:** 3 weeks of active development
- **Commits:** Multiple organized commits
- **Lines of Code:** Backend + Frontend + Templates
- **Active Branches:** 3 development branches
- **Documentation:** 7 technical documentation files

---

## 9. What We Learned

### Key Learnings
- Collaboration using Git with individual branches
- Frontend-Backend integration with Django
- Data visualization with Chart.js
- Authentication and route protection
- Team coordination and code integration

### Challenges We Solved
- Coordinating work between multiple developers
- Merging code from different branches
- Implementing dynamic charts
- Form validation on frontend and backend

---

## 10. Demo Suggestions

For the presentation, we recommend showing:

1. **Complete user flow:**
   - Fill out survey form
   - See thank you page
   - Access results dashboard (with login)

2. **Admin panel:**
   - Show list of responses
   - Demonstrate available filters

3. **Technical code (optional):**
   - File structure
   - Database model
   - Chart.js template

---

## 11. Key Features Summary

### User Features
- Simple and clean survey form
- Immediate feedback after submission
- Visual data representation with charts
- Mobile-responsive design

### Admin Features
- Secure login system
- Full control over survey data
- Filter and search capabilities
- Data export via Django Admin

### Technical Features
- RESTful URL structure
- Secure authentication
- Database validation
- Responsive design
- Interactive visualizations

---

## 12. Screenshots Reference

**What to show during presentation:**

1. **Survey Form Page:**
   - Show the 5 option cards
   - Demonstrate "Other" text field appearing
   - Fill out personal information

2. **Thank You Page:**
   - Success message
   - Button to explore results

3. **Results Dashboard:**
   - Total responses counter
   - Bar chart (reasons)
   - Doughnut chart (age groups)

4. **Admin Panel:**
   - List of all responses
   - Filter sidebar
   - Individual response details

---

**Prepared by:** Ireland Survey Team
**Date:** March 2026
**Module:** M2.8 DevOps - Dorset College
