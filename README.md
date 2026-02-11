# Django Portfolio Website

A modern **personal portfolio** built with **Django**.  
Fully dynamic content managed via the admin panel and a backend-focused architecture showcasing REST APIs, testing, and production deployment.

[![Django](https://img.shields.io/badge/Django-5.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15+-ff1709?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://neon.tech/)
![SQLite](https://img.shields.io/badge/SQLite-07405E?logo=sqlite&logoColor=white&style=for-the-badge)
[![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **Frontend Note**  
> The visual design (HTML/CSS/JS with cyberpunk effects, matrix rain, particles, etc.) is based on a customized template.  
> **I built and integrated the complete Django backend**: models, views, admin customization, DRF APIs, unit tests, form handling, environment config, Whitenoise static serving, Neon PostgreSQL integration, and Render deployment.

## Features

### Backend & Core
- **Dynamic Admin Content Management** — Manage homepage, about section, skills, projects, and contact messages directly from `/admin/`
- **RESTful API Endpoints** (DRF) — `/api/projects/`, `/api/skills/`, `/api/about/<id>/` for listing & creating content (JSON serialization)
- **Unit Testing** — Comprehensive tests for models, views, forms, and admin using Django's test framework
- **Contact Form with Email Notifications** — Secure form submission with validation and console/email backend (async-ready structure via Celery setup in dev)
- **Responsive & Animated UI** — Mobile-friendly with cyber gradient, matrix rain, data streams, orbs, and glitch effects
- **SEO & Settings** — Dynamic title, meta, keywords from admin-controlled Setting model

## Tech Stack

- **Backend**: Django 5.2+, Django REST Framework
- **Database**: SQLite (dev) → PostgreSQL (prod)
- **Frontend**: HTML5, CSS3, JavaScript
- **Testing**: Django Test Framework / Pytest compatible
- **Tools**: Git, Whitenoise, python-dotenv, CKEditor

## Requirements

The following software must be installed on your system to run the project:

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv
- Git
  
> **Note:**  
> Some systems use `python` instead of `python3`.  
> If any command fails, try replacing `python3` with `python`.

## Installation

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

You need to create a .env file in the project root, or rename the .env.example file and update its secret key with your own values.
The project will not run without this file.

Use the provided template as a starting point and replace all placeholder values with your own credentials.

```env
SECRET_KEY=your-secret-key
# Generate a secure one:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 8. Start Development Server

```bash
python3 manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser to view your site.

## Admin Panel Usage

### Accessing the Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin` in your browser
2. Log in with your superuser credentials

### Manageable Content

- **Homepage**  
  Update the main hero section title and content (RichTextField support).

- **About**  
  Edit your biography and professional story.  
  - Biography (rich text)  
  - **Skills** (inline editing – add/remove skills directly)  
  - Experience highlights

- **Projects**  
  Showcase your work with full control:  
  - Title  
  - Detailed description (RichTextField)  
  - External link (e.g., GitHub repo or live demo)  
  Add, edit, reorder, or delete projects easily.

- **Settings**  
  Control global site metadata:  
  - Site title  
  - Description & keywords (for SEO)  
  - Contact email & address

- **Contact Messages**  
  View and manage incoming messages from the contact form:  
  - Sender full name & email  
  - Message content  
  - Received date/time  
  - Read/unread status
