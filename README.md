# Django To-Do App

A simple Django project to practice building a To-Do application with:

- Basic CRUD operations (Create, Read, Update, Delete)
- A RESTful API for tasks
- Django Crispy Forms using Bootstrap 4 for form styling

---

## Features

- **Add**, **view**, **edit**, and **delete** tasks via web forms
- API endpoints to perform CRUD on tasks (using Django REST Framework or Django views)
- Forms styled with Bootstrap 4 through Django Crispy Forms
- SQLite database 

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtual environment tool (recommended: `venv`)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/django-todo-app.git
   cd django-todo-app
   ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate       # macOS/Linux
    venv\Scripts\activate          # Windows
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply migrations**
    ```bash
    python manage.py migrate
    ```
5. **Run the development server**
    ```bash
    python manage.py runserver
    ```
6. **Access the app**
    ```bash
    Open your browser at http://localhost:8000
    ```

**Usage**
- Use the web interface to create, update, and delete tasks.
- Forms are styled with Bootstrap 4 via Django Crispy Forms for a simple clean look.