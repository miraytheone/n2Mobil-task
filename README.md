# n2Mobil-task

This project is a web application developed using Vue.js and Django, storing data using PostgreSQL database.

## Requirements

- Node.js
- Python
- Django
- PostgreSQL

## Installation

1. **Clone the project:**
    ```bash
    git clone https://github.com/username/project_name.git
    cd project_name
    ```

2. **For the backend, create a virtual environment and install the required Python packages:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Install PostgreSQL database and configure your database settings in `backend/settings.py`.**

4. **Migrate the database:**
    ```bash
    python manage.py migrate
    ```

5. **For the frontend, navigate to the `frontend` directory and install the required packages:**
    ```bash
    cd ../frontend
    npm install
    ```

6. **Start the frontend:**
    ```bash
    npm run serve
    ```

7. **Start the backend:**
    ```bash
    python manage.py runserver
    ```

8. **Visit `http://localhost:8080` in your browser to view the application.**

## Usage

After starting the application, add a description of the functionalities/features on the home page.

These installation steps provide a general guide on how to run the project in a local environment. You can customize the steps according to the specific requirements and configuration of the project.
