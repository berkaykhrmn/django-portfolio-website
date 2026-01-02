# 🚀 Portfolio Website with Django

A modern and dynamic personal portfolio website built with the Django framework. It features a fully responsive design and easy content management through the Django admin panel, allowing you to showcase your projects and Django development skills effectively.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Note:**
> The HTML–CSS–JS design of this website is based on a pre-made template. I integrated the Django backend myself and customized the template to fit my personal portfolio structure. All backend logic, models, admin configuration, and dynamic content features were developed by me.

## ✨ Features

### 🎯 Core Features
- **Dynamic Content Management**: All content managed through Django admin panel
- **Project Showcase**: Display your projects with visuals and detailed descriptions
- **Responsive Design**: Perfect appearance across all devices
- **Working Contact Form**: Connect with visitors through a functional contact form
- **About Section**: Share your story, skills, and experience

### 🛠️ Technical Features
- Django framework
- SQLite database
- Responsive frontend with Bootstrap
- Django Admin panel integration
- Form validation and security measures
- Static and media file management

## 📋 Requirements

The following software must be installed on your system to run the project:

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv
- Git
  
> **Note:**  
> Some systems use `python` instead of `python3`.  
> If any command fails, try replacing `python3` with `python`.

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/berkaykhrmn/django-portfolio-website.git
cd django-portfolio-website
```

### 2. Create Virtual Environment

**Windows:**
```bash
python3 -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Database

The SQLite database will be created automatically when you run migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
**Note:** The `db.sqlite3` file is automatically generated and should not be committed to version control. Make sure it's listed in your `.gitignore` file.

### 5. Create Superuser

Create a superuser account to access the admin panel:

```bash
python3 manage.py createsuperuser
```
Enter your username, email, and password when prompted.

### 6. Collect Static Files

```bash
python3 manage.py collectstatic
```

### 7. Environment Variables

You must create a `.env` file in the project root.  
The project will not work without this file.

Use the template below as a starting point.  
Replace the placeholder values with your own credentials.

```env
# Django Secret Key → MUST be changed!
SECRET_KEY=replace_this_with_a_real_secret_key
# Generate a secure one:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Development mode
IS_DEV=True

# Local development
APP_HOST=127.0.0.1

# ───────────────────────────────
# Gmail SMTP Configuration
# ───────────────────────────────
HOST_USER=your-email@gmail.com
HOST_PASS=your-16-digit-gmail-app-password

# How to get HOST_PASS:
# 1. Enable 2-Factor Authentication on your Google account
# 2. Go to → https://myaccount.google.com/apppasswords
# 3. Create an app password (select "Mail" and your device)
# 4. Copy the 16-digit password (ignore spaces) and paste here
```

### 8. Start Development Server

```bash
python3 manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser to view your site.

## 👨‍💼 Admin Panel Usage

### Accessing the Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin` in your browser
2. Log in with your superuser credentials

### Content Management

From the admin panel, you can manage the following content:

- **Projects**: Add, edit, or delete projects
  - Project name and description
  - Technologies used
  - Project link and GitHub repository
  
- **About**: Update your personal information
  - Biography
  - Skills
  - Experience
   
- **Contact Messages**: View messages from visitors
  - Message details
  - Sender information
  - Date and time

