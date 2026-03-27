# Complete Deploy Guide to Render

This guide will help you deploy the Ireland Survey project to Render (a free hosting platform). **No previous deployment experience needed!**

---

## What is Render?

Render is a cloud platform where you can host web applications for free. It's perfect for student projects and small applications.

**Why Render?**
- ✅ Free forever for small projects
- ✅ Automatic deployment from GitHub
- ✅ HTTPS (secure connection) included
- ✅ Easy to use
- ✅ No credit card required

---

## Before You Start

Make sure you have:

- [x] GitHub account (you already have this)
- [x] Updated project code (run `git pull origin main`)
- [x] 15-20 minutes of free time

**Important:** All configuration files are already prepared in the repository. You just need to follow this guide to deploy!

---

## Step 1: Pull Latest Changes

First, make sure you have all the latest deployment files:

```bash
cd ~/projects/research_project
git checkout your-branch-name
git pull origin main
```

You should see these files in your project:
- ✅ `runtime.txt` - Python version configuration
- ✅ `build.sh` - Build script for Render
- ✅ `requirements.txt` - Updated with deployment packages
- ✅ `settings.py` - Already configured for production

**Everything is ready! Let's deploy!** 🚀

---

## Step 2: Create a Render Account

1. Go to https://render.com
2. Click **"Get Started for Free"** or **"Sign Up"**
3. Choose **"Sign up with GitHub"** (easiest option)
4. Authorize Render to access your GitHub account
5. You're now logged in to Render!

---

## Step 3: Create a New Web Service

### 3.1 Connect Your Repository

1. On the Render Dashboard, click **"New +"** button (top right)
2. Select **"Web Service"**
3. You'll see a list of your GitHub repositories
4. Find **"research_project"** and click **"Connect"**

**If you don't see your repository:**
- Click **"Configure account"** at the bottom
- Select your GitHub username
- Choose **"All repositories"** or select **"research_project"**
- Click **"Save"**

---

### 3.2 Configure Your Web Service

Now you'll see a form. Fill it out exactly as shown below:

#### Basic Settings:

| Field | Value |
|-------|-------|
| **Name** | `ireland-survey` (or any name you like, lowercase, no spaces) |
| **Region** | Choose the one closest to Ireland (e.g., Frankfurt) |
| **Branch** | `main` |
| **Root Directory** | Leave empty |
| **Runtime** | Python 3 |

#### Build & Deploy Settings:

| Field | Value |
|-------|-------|
| **Build Command** | `bash build.sh` |
| **Start Command** | `gunicorn ireland_survey.wsgi:application` |

#### Plan:

- Select **"Free"** plan (should be already selected)

---

### 3.3 Add Environment Variables

Scroll down to **"Environment Variables"** section.

Click **"Add Environment Variable"** and add these:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | `your-secret-key-here` (you can copy from your current settings.py) |
| `DEBUG` | `False` |

**Important:** For `SECRET_KEY`, you can generate a new one or copy the existing one from your `settings.py` file.

To generate a new secret key, you can use this online tool:
https://djecrety.ir/

---

### 3.4 Create Web Service

After filling everything:

1. Review all settings
2. Click **"Create Web Service"** button at the bottom

**What happens now:**
- Render will start building your application
- You'll see a log screen with messages
- This process takes **5-10 minutes**
- Wait until you see **"Build successful"** and **"Deploy live"**

---

## Step 4: Create Admin User in Production

Once your app is deployed, you need to create an admin user to access `/admin/`.

### 4.1 Open Render Shell

1. On your Render service page, click **"Shell"** tab at the top
2. A terminal will open

### 4.2 Create Superuser

Type this command in the shell:

```bash
python manage.py createsuperuser
```

Follow the prompts:
- **Username:** `admin`
- **Email:** (press Enter to skip or add any email)
- **Password:** `123` (or choose a secure password)
- **Password (again):** `123`

**Note:** The password won't show while typing - this is normal.

When done, you'll see: **"Superuser created successfully"**

---

## Step 5: Test Your Deployed Application

Your app is now live! 🎉

### Find Your App URL

At the top of the Render dashboard, you'll see your app URL:

```
https://ireland-survey.onrender.com
```

(The exact URL depends on the name you chose)

### Test These Pages:

1. **Survey Form:** `https://your-app-name.onrender.com/`
   - Fill out and submit a survey

2. **Thank You Page:** `https://your-app-name.onrender.com/thanks/`
   - Should redirect here after submitting

3. **Results Dashboard:** `https://your-app-name.onrender.com/results/`
   - Should show charts (might be empty if no responses yet)

4. **Admin Panel:** `https://your-app-name.onrender.com/admin/`
   - Login with username: `admin`, password: `123`
   - Check if your test response appears here

---

## Step 6: Share Your Survey

Now you can share your survey with classmates!

### Generate QR Code

1. Copy your survey URL: `https://your-app-name.onrender.com/`
2. Go to: https://www.qr-code-generator.com/
3. Paste your URL
4. Click **"Create QR Code"**
5. Download and print the QR code

People can scan the QR code with their phones and access your survey instantly!

---

## How to Update Your App

Every time you make changes to your code and push to GitHub:

```bash
git add .
git commit -m "Your change description"
git push origin main
```

**Render will automatically:**
- Detect the changes
- Rebuild your app
- Deploy the new version

You can watch the progress in the **"Logs"** tab on Render.

---

## Important Notes

### App "Sleeping"

On the free plan, your app will "sleep" after 15 minutes of inactivity.

**What this means:**
- First visitor after sleep = 30-60 seconds loading time
- After that = normal speed
- This is normal for free tier

**Tip:** Before your class presentation, open the URL once to "wake it up".

---

### Database Persistence

Render free tier uses SQLite database which resets periodically.

**What this means:**
- Survey responses might be lost after some time
- For a student project, this is acceptable
- Collect responses and take screenshots regularly

**Better option (optional):**
If you need permanent data storage, you can upgrade to PostgreSQL (also free on Render).

---

## Troubleshooting

### Problem: "Application failed to start"

**Solution:**
1. Go to **"Logs"** tab on Render
2. Look for error messages
3. Common issues:
   - Missing package in `requirements.txt`
   - Wrong build command
   - Python version mismatch

### Problem: "Static files not loading (no CSS)"

**Solution:**
1. Check that `whitenoise` is in `requirements.txt`
2. Check that `whitenoise` middleware is in `settings.py`
3. Rebuild: Go to **"Manual Deploy"** → **"Clear build cache & deploy"**

### Problem: "Can't create superuser"

**Solution:**
1. Make sure deployment is complete (shows "Deploy live")
2. Wait 1-2 minutes after deployment
3. Try the shell command again

### Problem: "ALLOWED_HOSTS error"

**Solution:**
1. Make sure `ALLOWED_HOSTS = ['*']` in settings.py
2. Push changes to GitHub
3. Wait for automatic redeployment

---

## Summary Checklist

Deployment checklist:

- [ ] Pulled latest changes from main branch (`git pull origin main`)
- [ ] Created Render account
- [ ] Connected GitHub repository to Render
- [ ] Configured web service correctly
- [ ] Added environment variables
- [ ] Waited for build to complete (5-10 minutes)
- [ ] Created admin user in production via Shell
- [ ] Tested all pages (survey, thanks, results, admin)
- [ ] Generated QR code for sharing

---

## Getting Help

**If something doesn't work:**

1. Check the **"Logs"** tab on Render for error messages
2. Google the error message
3. Check Render documentation: https://render.com/docs
4. Contact Paulo (team leader)

---

## Deployment Success!

Once everything works:

✅ Your survey is live on the internet
✅ Anyone can access it via URL or QR code
✅ Data is being collected in the database
✅ You can show it in your presentation

**Congratulations!** 🎉

---

## Extra: Production Best Practices (Optional)

If you want to make your deployment more secure and professional:

### 1. Use Environment Variables for Sensitive Data

Instead of hardcoding `SECRET_KEY` in settings.py, use:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

### 2. Set Specific ALLOWED_HOSTS

After deployment, replace:
```python
ALLOWED_HOSTS = ['*']
```

With:
```python
ALLOWED_HOSTS = ['ireland-survey.onrender.com', 'localhost', '127.0.0.1']
```

### 3. Monitor Your App

Check the **"Metrics"** tab on Render to see:
- Number of requests
- Response times
- CPU and memory usage

---

**Good luck with your deployment!** 🚀

**Prepared by:** Ireland Survey Team
**Date:** March 2026
**Module:** M2.8 DevOps - Dorset College
