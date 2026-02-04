# Ireland Immigration Survey — Project Roadmap

## 1. Project Overview

### What We Are Building

A simple Django web application to collect survey responses about why people chose to live in Ireland. The system consists of **3 public/protected screens** and uses **Django Admin** as the backend management interface.

**Survey Topic:** *"Why did you choose to live in Ireland?"*

---

### Screen Descriptions

| Screen | URL | Description |
|--------|-----|-------------|
| **Survey Form** | `/` | Main question with 5 predefined options + "Other" with text field. Collects 5 personal fields. Submits to database. |
| **Thank You** | `/thanks/` | Confirmation message after submission. Button to explore results. |
| **Results Dashboard** | `/results/` | Aggregated data: total respondents, chart by reason, chart by age group. **Login required.** |
| **Admin Panel** | `/admin/` | Django Admin for managing responses (built-in). |

---

### Main Question Options

1. Learn English
2. Job Opportunities
3. Quality of Life
4. Career / Future
5. Other (with text field: "Please specify")

### Personal Information Fields

1. Full Name
2. Age
3. Email
4. Nationality
5. Current City in Ireland

---

## 2. Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Backend language |
| Django 4.x | Web framework |
| Bootstrap 5 | Frontend styling (clean, modern UI) |
| SQLite | Database (default, simple) |
| Chart.js | Charts on results page |
| EasyPanel | Deployment platform |
| Docker | Optional containerization |

---

## 3. Team Structure

| Member | Role | Branch Name |
|--------|------|-------------|
| **Paulo** | Team Leader, Git Manager, Code Reviewer | `paulo` |
| **Larissa** | Developer | `larissa` |
| **Lucas** | Developer | `lucas` |
| **Matheus** | Developer | `matheus` |
| **Humberto** | Developer | `humberto` |

---

## 4. Git/GitHub Workflow

### Branch Strategy

```
main (protected - Paulo only)
  ├── paulo
  ├── larissa
  ├── lucas
  ├── matheus
  └── humberto
```

### Rules

1. **Never commit directly to `main`** — all team members work on their own branch
2. **All changes require a Pull Request (PR)** to merge into `main`
3. **Paulo reviews and approves all PRs** before merging
4. **Sync regularly** — run `git pull origin main` before starting new work

### Pull Request Requirements

Every PR must include:

- [ ] Clear title describing the change
- [ ] Description of what was done
- [ ] How to test locally (step-by-step)
- [ ] Screenshots (if UI was changed)
- [ ] No merge conflicts with `main`

### PR Template

```markdown
## What was done
- [Describe changes]

## How to test locally
1. Pull this branch
2. Run `python manage.py migrate`
3. Run `python manage.py runserver`
4. Go to [URL] and verify [behavior]

## Screenshots
[Attach if UI changed]
```

---

## 5. Implementation Roadmap

---

### Phase 0: Project Setup

**Goal:** Initialize Django project structure and configure repository

| Task | Assigned To | Branch |
|------|-------------|--------|
| Create Django project (`ireland_survey`) | Paulo | `paulo` |
| Create Django app (`survey`) | Paulo | `paulo` |
| Configure `settings.py` (allowed hosts, static files) | Paulo | `paulo` |
| Add `.gitignore` (Python/Django template) | Paulo | `paulo` |
| Create `requirements.txt` | Paulo | `paulo` |
| Add Bootstrap 5 CDN to base template | Paulo | `paulo` |
| Create `base.html` template with navbar | Paulo | `paulo` |
| Merge setup into `main` | Paulo | `main` |

**Definition of Done:**
- [ ] Django project runs locally with `python manage.py runserver`
- [ ] Base template renders with Bootstrap styling
- [ ] All team members can clone and run the project
- [ ] `.gitignore` excludes `db.sqlite3`, `__pycache__`, `.env`

---

### Phase 1: Database Model

**Goal:** Create the survey response model and register in Django Admin

| Task | Assigned To | Branch |
|------|-------------|--------|
| Create `SurveyResponse` model with all fields | Lucas | `lucas` |
| Add field choices for main question | Lucas | `lucas` |
| Create and run migrations | Lucas | `lucas` |
| Register model in `admin.py` | Lucas | `lucas` |
| Create superuser for testing | Lucas | `lucas` |
| Open PR → Paulo reviews and merges | Paulo | `main` |

**Model Fields:**
- `reason` (CharField with choices)
- `reason_other` (TextField, blank=True)
- `full_name` (CharField)
- `age` (IntegerField)
- `email` (EmailField)
- `nationality` (CharField)
- `city` (CharField)
- `created_at` (DateTimeField, auto_now_add)

**Definition of Done:**
- [ ] Model appears in Django Admin
- [ ] Can create/edit/delete responses via Admin
- [ ] All fields save correctly to database

---

### Phase 2: Survey Form Page (Screen 1)

**Goal:** Build the main survey form at `/`

| Task | Assigned To | Branch |
|------|-------------|--------|
| Create `SurveyForm` using Django ModelForm | Larissa | `larissa` |
| Create view for GET (show form) and POST (save + redirect) | Larissa | `larissa` |
| Create `survey_form.html` template | Larissa | `larissa` |
| Style form with Bootstrap (cards, spacing, buttons) | Larissa | `larissa` |
| Add JavaScript: show "Other" text field only when selected | Larissa | `larissa` |
| Add form validation (required fields, valid email) | Larissa | `larissa` |
| Configure URL route for `/` | Larissa | `larissa` |
| Open PR → Paulo reviews and merges | Paulo | `main` |

**Definition of Done:**
- [ ] Form displays all fields with proper labels
- [ ] "Other" text field appears/hides based on selection
- [ ] Form validates required fields
- [ ] Successful submission saves to database
- [ ] Redirects to `/thanks/` after submit
- [ ] Form is styled and mobile-responsive

---

### Phase 3: Thank You Page (Screen 2)

**Goal:** Build the confirmation page at `/thanks/`

| Task | Assigned To | Branch |
|------|-------------|--------|
| Create simple view for thank you page | Matheus | `matheus` |
| Create `thanks.html` template | Matheus | `matheus` |
| Add success icon/checkmark (Bootstrap icons or image) | Matheus | `matheus` |
| Add "Thank you for sharing your story" message | Matheus | `matheus` |
| Add button "Explore the Results" → links to `/results/` | Matheus | `matheus` |
| Style page to match overall design | Matheus | `matheus` |
| Configure URL route for `/thanks/` | Matheus | `matheus` |
| Open PR → Paulo reviews and merges | Paulo | `main` |

**Definition of Done:**
- [ ] Page displays thank you message
- [ ] Button navigates to results page
- [ ] Page is visually consistent with survey form
- [ ] Works on mobile devices

---

### Phase 4: Results Dashboard (Screen 3)

**Goal:** Build the protected results page at `/results/`

| Task | Assigned To | Branch |
|------|-------------|--------|
| Create view to aggregate survey data | Humberto | `humberto` |
| Calculate: total responses, count by reason, count by age group | Humberto | `humberto` |
| Create `results.html` template | Humberto | `humberto` |
| Display total respondents (card/stat box) | Humberto | `humberto` |
| Add Chart.js for "Reasons" bar/pie chart | Humberto | `humberto` |
| Add Chart.js for "Age Groups" chart (18-24, 25-34, 35+) | Humberto | `humberto` |
| Add `@login_required` decorator to protect page | Humberto | `humberto` |
| Configure URL route for `/results/` | Humberto | `humberto` |
| Open PR → Paulo reviews and merges | Paulo | `main` |

**Age Group Logic:**
- 18–24 years
- 25–34 years
- 35+ years

**Definition of Done:**
- [ ] Page shows total number of responses
- [ ] Chart displays count per reason
- [ ] Chart displays count per age group
- [ ] Page requires login to access
- [ ] Non-logged users are redirected to login page
- [ ] Charts render correctly with real data

---

### Phase 5: Authentication & Polish

**Goal:** Configure Django authentication and UI improvements

| Task | Assigned To | Branch |
|------|-------------|--------|
| Configure Django login view | Paulo | `paulo` |
| Create simple `login.html` template | Paulo | `paulo` |
| Add login/logout links to navbar | Paulo | `paulo` |
| Review all pages for UI consistency | Larissa | `larissa` |
| Add project footer with team info | Matheus | `matheus` |
| Test all navigation flows | All | — |
| Fix any bugs found | Assigned per bug | — |
| Open PRs → Paulo reviews and merges | Paulo | `main` |

**Definition of Done:**
- [ ] Login page works and styled with Bootstrap
- [ ] Results page redirects to login if not authenticated
- [ ] Navbar shows correct links based on login state
- [ ] All pages have consistent styling
- [ ] No broken links or navigation errors

---

### Phase 6: Testing & Quality Assurance

**Goal:** Verify all functionality works correctly

| Task | Assigned To | Branch |
|------|-------------|--------|
| Test survey form with valid data | Lucas | — |
| Test survey form with invalid data (validation) | Lucas | — |
| Test "Other" option shows/hides text field | Larissa | — |
| Test thank you page redirect | Matheus | — |
| Test results page with 0 responses | Humberto | — |
| Test results page with multiple responses | Humberto | — |
| Test login protection on results page | Paulo | — |
| Test on mobile device/responsive | All | — |
| Document any bugs found | All | — |
| Fix critical bugs | Assigned per bug | — |

**Definition of Done:**
- [ ] All core features work as expected
- [ ] No critical bugs remaining
- [ ] Application works on desktop and mobile
- [ ] All team members have tested locally

---

### Phase 7: Deployment (Optional)

**Goal:** Deploy application to EasyPanel for real-world testing

| Task | Assigned To | Branch |
|------|-------------|--------|
| Create `Dockerfile` for Django app | Paulo | `paulo` |
| Create `docker-compose.yml` (optional) | Paulo | `paulo` |
| Configure production settings (DEBUG=False, ALLOWED_HOSTS) | Paulo | `paulo` |
| Set up EasyPanel project | Paulo | — |
| Deploy application to EasyPanel | Paulo | — |
| Configure environment variables | Paulo | — |
| Test deployed application | All | — |
| Generate QR code for survey URL | Paulo | — |

**Definition of Done:**
- [ ] Application accessible via public URL
- [ ] Survey form works in production
- [ ] Results page works with login
- [ ] QR code generated and ready for sharing

---

### Phase 8: Data Collection & Documentation

**Goal:** Collect real responses and prepare final documentation

| Task | Assigned To | Branch |
|------|-------------|--------|
| Share QR code with classmates/friends | All | — |
| Collect minimum 20-30 responses | All | — |
| Take screenshots of results dashboard | Humberto | — |
| Write project summary for CA2 report | All | — |
| Document DevOps practices used | All | — |
| Prepare work diary entries | Individual | — |

**Definition of Done:**
- [ ] Minimum 20 survey responses collected
- [ ] Screenshots of working application saved
- [ ] Each team member has 10 diary entries
- [ ] Project documentation complete

---

## 6. Summary: Task Distribution

| Member | Primary Responsibilities |
|--------|-------------------------|
| **Paulo** | Project setup, Git management, authentication, deployment, PR reviews |
| **Larissa** | Survey form (Screen 1), form validation, UI polish |
| **Lucas** | Database model, Django Admin, testing |
| **Matheus** | Thank you page (Screen 2), footer, UI elements |
| **Humberto** | Results dashboard (Screen 3), charts, data aggregation |

---

## 7. Timeline Suggestion

| Phase | Description | Duration |
|-------|-------------|----------|
| Phase 0 | Project Setup | Day 1-2 |
| Phase 1 | Database Model | Day 3-4 |
| Phase 2 | Survey Form | Day 5-7 |
| Phase 3 | Thank You Page | Day 5-6 |
| Phase 4 | Results Dashboard | Day 7-10 |
| Phase 5 | Auth & Polish | Day 11-12 |
| Phase 6 | Testing | Day 13-14 |
| Phase 7 | Deployment | Day 15-16 |
| Phase 8 | Data Collection | Day 17+ |

---

## 8. QR Code Sharing Plan

1. Deploy final application to EasyPanel
2. Copy the public URL (e.g., `https://ireland-survey.easypanel.io`)
3. Generate QR code using free tool (e.g., qr-code-generator.com)
4. Print QR code or share digitally
5. Distribute to classmates during class
6. Monitor responses via Django Admin or Results page
7. Celebrate reaching 30+ responses

---

**End of Roadmap**
