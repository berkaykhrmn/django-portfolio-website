# Portfolio Website with Django

A modern and dynamic personal portfolio website built with the Django framework. It features a fully responsive design and easy content management through the Django admin panel, allowing you to showcase your projects and Django development skills effectively.

![Django](https://img.shields.io/badge/Django-6.0+-092E20?logo=django&logoColor=white&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white&style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white&style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?logo=sqlite&logoColor=white&style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?logo=bootstrap&logoColor=white&style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white&style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> **Note:**
> The frontend (HTML, CSS, JavaScript) of this project is based on a pre-made template.
I integrated and developed the entire Django backend architecture, including models, admin configuration, database design, environment configuration, and all dynamic content features.
The template was customized and adapted to fit the project’s structure and functionality.

## Features

### Core Features
- **Dynamic Content Management**: All content managed through Django admin panel
- **Project Showcase**: Display your projects with visuals and detailed descriptions
- **Responsive Design**: Perfect appearance across all devices
- **Working Contact Form**: Connect with visitors through a functional contact form
- **About Section**: Share your story, skills, and experience

### Technical Features
- Django framework
- SQLite database (PostgreSQL for Deployment)
- Responsive frontend with Bootstrap
- Django Admin panel integration
- Form validation and security measures
- Static and media file management

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

