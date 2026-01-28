# Getting Started Guide

Welcome to the **Research Project** team! This document will guide you through the initial setup to start collaborating.

## Prerequisites

Before you begin, make sure you have:

- Git installed on your computer
- A GitHub account
- Been added as a collaborator to this repository

### Installing Git

**Windows:**
1. Download Git from https://git-scm.com/download/win
2. Run the installer and follow the instructions

**Mac:**
```bash
brew install git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install git
```

---

## Task 1: Clone the Repository

Follow these steps to get a local copy of the project on your computer.

### Step 1: Create a folder for the project

Open your terminal (or Git Bash on Windows) and create a folder where you want to store the project:

```bash
mkdir ~/projects
cd ~/projects
```

### Step 2: Clone the repository

Run the following command to download the project:

```bash
git clone https://github.com/paulo9405/research_project.git
```

### Step 3: Enter the project folder

```bash
cd research_project
```

### Step 4: Verify the setup

Check that everything is working correctly:

```bash
git status
```

You should see a message like: `On branch main` and `nothing to commit, working tree clean`.

---

## Task 2: Switch to Your Branch

Each team member has their own branch. Find your name below and switch to your branch.

### Branch Assignments

| Team Member | Branch Name |
|-------------|-------------|
| Lucas | `lucas` |
| Larissa | `larissa` |
| Humberto | `humberto` |
| Matheus | `matheus` |

### Step 1: Switch to your branch

Replace `your-branch-name` with your assigned branch from the table above:

```bash
git checkout your-branch-name
```

**Example for Lucas:**
```bash
git checkout lucas
```

### Step 2: Verify you are on the correct branch

```bash
git branch
```

You should see an asterisk (*) next to your branch name, like this:
```
  main
* lucas
```

---

## Task 3: Making Changes and Pushing

When you make changes to the project, follow these steps:

### Step 1: Check what files you modified

```bash
git status
```

### Step 2: Add your changes

```bash
git add .
```

### Step 3: Commit your changes

```bash
git commit -m "Describe what you changed"
```

### Step 4: Push to GitHub

```bash
git push
```

---

## Important Rules

1. **Never commit directly to the `main` branch**
2. Always work on your assigned branch
3. Only the project leader manages the `main` branch
4. Write clear commit messages describing your changes
5. Push your changes regularly to keep the repository updated

---

## Need Help?

If you encounter any issues during setup, contact the project leader.

---

**Important:** Only the project leader manages the `main` branch. Always work on your assigned branch.
