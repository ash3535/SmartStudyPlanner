# 📚 Smart Study Planner

A full-stack study management web application built with **Python, Flask, and PostgreSQL**.

Smart Study Planner helps students organize study tasks, track their progress, and automatically generate a prioritized study plan based on deadlines, priority, difficulty, and estimated study time.

## 🚀 Features

### 🔐 User Authentication

* User registration and login
* Secure password hashing
* Session-based authentication
* Logout functionality
* User-specific study tasks
* Users can only access their own tasks

### 📝 Study Task Management

* Add study tasks
* View study tasks
* Update study tasks
* Delete study tasks
* Mark tasks as completed
* Completed tasks are automatically shown at the bottom
* Input validation for task information

### 🧠 Smart Study Plan

The application automatically prioritizes pending study tasks based on:

* Deadline
* Priority
* Difficulty
* Estimated study hours

Each task receives a priority score, and tasks are arranged from the highest score to the lowest.

### 📊 Study Dashboard

The dashboard provides:

* Total number of tasks
* Pending tasks
* Completed tasks
* High-priority tasks
* Total study hours
* Completion rate

### 🔒 Security

* Passwords are stored using secure hashing
* PostgreSQL credentials are stored in environment variables
* Flask secret key is stored in `.env`
* `.env` is excluded from Git
* Database queries use parameterized SQL
* Tasks are isolated between users

## 🛠️ Technologies Used

* **Python** — Application logic
* **Flask** — Web framework
* **PostgreSQL** — Database
* **psycopg2** — PostgreSQL connection
* **HTML** — Web interface
* **CSS** — Styling
* **Jinja2** — Dynamic HTML templates
* **Git & GitHub** — Version control
* **python-dotenv** — Environment configuration

## 📁 Project Structure

```text
SmartStudyPlanner/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── task_manager.py
│   ├── user_manager.py
│   ├── planner.py
│   │
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── plan.html
│   │   └── dashboard.html
│   │
│   └── static/
│       └── style.css
│
├── tests/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

## 🗄️ Database

The application uses PostgreSQL.

Users Table

Stores account information for each user.

Stores study tasks created by users.

Each user can have multiple study tasks.

Study Tasks Table

Stores study tasks created by users.

    ┌───────────────┐
    │     users     │
    ├───────────────┤
    │ id (PK)       │
    │ username      │
    │ email         │
    │ password_hash │
    │ created_at    │
    └───────┬───────┘
            │
            │ 1 : Many
            │
            ▼
    ┌────────────────────┐
    │    study_tasks     │
    ├────────────────────┤
    │ id (PK)            │
    │ title              │
    │ subject            │
    │ difficulty         │
    │ estimated_hours    │
    │ deadline           │
    │ priority           │
    │ completed          │
    │ user_id (FK)       │
    └────────────────────┘

Primary Key (PK): Uniquely identifies each record.

Foreign Key (FK): study_tasks.user_id connects each task to its owner in the users table.

This relationship ensures that each logged-in user can access and manage their own study tasks.

## 🧠 Smart Prioritization

The study planner calculates a score for every pending task.

```text
Total Score =
    Deadline Score
    + Priority Score
    + Difficulty Score
    + Study Hours Score
```

### Priority Scores

```text
High   → 10
Medium → 5
Low    → 2
```

### Difficulty Scores

```text
Hard   → 6
Medium → 4
Easy   → 2
```

Tasks with closer deadlines receive higher deadline scores.

Estimated study hours also contribute to the score, with the contribution limited to 10 points.

The final score is used to arrange pending tasks in the Smart Study Plan.

## 🔐 Authentication Flow

```text
User Signup
     ↓
Password Hashing
     ↓
PostgreSQL
     ↓
User Login
     ↓
Password Verification
     ↓
Flask Session
     ↓
User-specific Tasks
```

Each task operation checks the logged-in user's ID.

For example, task updates and deletions use both the task ID and user ID. This prevents one user from modifying another user's tasks.

## 📊 Application Flow

```text
                    ┌─────────────┐
                    │   Signup    │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │    Login    │
                    └──────┬──────┘
                           ↓
                 ┌───────────────────┐
                 │   Study Tasks     │
                 └─────────┬─────────┘
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
         Task CRUD     Smart Plan    Dashboard
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd SmartStudyPlanner
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the PostgreSQL database

Create a PostgreSQL database named:

```text
smart_study_planner
```

Create the required tables using the SQL shown in the **Database** section.

### 6. Configure environment variables

Create a `.env` file in the project root:

```text
DB_HOST=localhost
DB_NAME=smart_study_planner
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_PORT=5432
SECRET_KEY=your_secret_key
```

Do not commit `.env` to GitHub.

### 7. Run the application

```powershell
python app/main.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

* Python
* Object-Oriented Programming
* Flask
* PostgreSQL
* SQL
* CRUD operations
* Database relationships
* Authentication
* Password hashing
* Flask sessions
* Form validation
* Jinja2 templates
* Environment variables
* Git & GitHub
* Backend application structure

## 🔮 Future Improvements

Possible future improvements:

* Subject-wise statistics
* Study session tracking
* Daily study goals
* Calendar integration
* Study reminders
* REST API
* Charts and visual analytics
* Search and filtering
* Automated testing
* Cloud deployment

## 👨‍💻 Author

**Ash**

A Python portfolio project focused on backend development, PostgreSQL, authentication, and practical web application development.
