import os

from flask import Flask, render_template, request, redirect, flash, session
from dotenv import load_dotenv

from models import StudyTask
from task_manager import TaskManager
from planner import create_study_plan
from user_manager import UserManager


load_dotenv()


app = Flask(__name__)

app.secret_key = os.getenv(
    "SECRET_KEY",
    "smart-study-planner-secret-key"
)

manager = TaskManager()
user_manager = UserManager()

def login_required():

    if "user_id" not in session:
        return False

    return True

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "GET":
        return render_template("signup.html")

    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    if not username or not email or not password or not confirm_password:
        flash("Please fill in all fields.", "error")
        return redirect("/signup")

    if len(username) < 3:
        flash("Username must be at least 3 characters.", "error")
        return redirect("/signup")

    if len(password) < 6:
        flash("Password must be at least 6 characters.", "error")
        return redirect("/signup")

    if password != confirm_password:
        flash("Passwords do not match.", "error")
        return redirect("/signup")

    user_id = user_manager.create_user(
        username,
        email,
        password
    )

    if not user_id:
        flash("Username or email already exists.", "error")
        return redirect("/signup")

    session["user_id"] = user_id
    session["username"] = username

    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    username_or_email = request.form.get(
        "username_or_email",
        ""
    ).strip()

    password = request.form.get(
        "password",
        ""
    )

    if not username_or_email or not password:
        flash(
            "Please enter your username/email and password.",
            "error"
        )
        return redirect("/login")

    user = user_manager.authenticate_user(
        username_or_email,
        password
    )

    if not user:
        flash(
            "Invalid username/email or password.",
            "error"
        )
        return redirect("/login")

    session["user_id"] = user[0]
    session["username"] = user[1]

    return redirect("/")

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "You have been logged out.",
        "success"
    )

    return redirect("/login")

@app.route("/")
def home():

    if not login_required():
        return redirect("/login")

    tasks = manager.get_tasks(
        session["user_id"]
    )

    return render_template(
        "index.html",
        tasks=tasks
    )


@app.route("/add", methods=["POST"])
def add_task():

    if not login_required():
        return redirect("/login")

    try:

        title = request.form.get("title", "").strip()
        subject = request.form.get("subject", "").strip()
        difficulty = request.form.get("difficulty", "")

        estimated_hours = float(
            request.form.get("estimated_hours", 0)
        )

        deadline = request.form.get("deadline", "")
        priority = request.form.get("priority", "")

        if not title or not subject or not deadline:
            flash(
                "Please fill in all required fields.",
                "error"
            )
            return redirect("/")

        if estimated_hours <= 0:
            flash(
                "Study hours must be greater than 0.",
                "error"
            )
            return redirect("/")

        if difficulty not in ["Easy", "Medium", "Hard"]:
            flash(
                "Invalid difficulty selected.",
                "error"
            )
            return redirect("/")

        if priority not in ["Low", "Medium", "High"]:
            flash(
                "Invalid priority selected.",
                "error"
            )
            return redirect("/")

        task = StudyTask(
            title,
            subject,
            difficulty,
            estimated_hours,
            deadline,
            priority
        )

        manager.add_task(
            task,
            session["user_id"]
        )

        flash(
            "Task added successfully!",
            "success"
        )

    except ValueError:

        flash(
            "Please enter a valid number for study hours.",
            "error"
        )

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    if not login_required():
        return redirect("/login")

    manager.delete_task(
        task_id,
        session["user_id"]
    )

    flash(
        "Task deleted.",
        "success"
    )

    return redirect("/")


@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):

    if not login_required():
        return redirect("/login")

    try:

        title = request.form.get("title", "").strip()
        subject = request.form.get("subject", "").strip()
        difficulty = request.form.get("difficulty", "")

        estimated_hours = float(
            request.form.get("estimated_hours", 0)
        )

        deadline = request.form.get("deadline", "")
        priority = request.form.get("priority", "")

        if not title or not subject or not deadline:
            flash(
                "Please fill in all required fields.",
                "error"
            )
            return redirect("/")

        if estimated_hours <= 0:
            flash(
                "Study hours must be greater than 0.",
                "error"
            )
            return redirect("/")

        if difficulty not in ["Easy", "Medium", "Hard"]:
            flash(
                "Invalid difficulty selected.",
                "error"
            )
            return redirect("/")

        if priority not in ["Low", "Medium", "High"]:
            flash(
                "Invalid priority selected.",
                "error"
            )
            return redirect("/")

        manager.update_task(
            task_id,
            session["user_id"],
            title,
            subject,
            difficulty,
            estimated_hours,
            deadline,
            priority
        )

        flash(
            "Task updated successfully!",
            "success"
        )

    except ValueError:

        flash(
            "Please enter a valid number for study hours.",
            "error"
        )

    return redirect("/")


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):

    if not login_required():
        return redirect("/login")

    manager.toggle_task(
        task_id,
        session["user_id"]
    )

    return redirect("/")


@app.route("/plan")
def study_plan():

    if not login_required():
        return redirect("/login")

    tasks = manager.get_tasks(
        session["user_id"]
    )

    planned_tasks = create_study_plan(tasks)

    return render_template(
        "plan.html",
        tasks=planned_tasks
    )


@app.route("/dashboard")
def dashboard():

    if not login_required():
        return redirect("/login")

    statistics = manager.get_statistics(
        session["user_id"]
    )

    return render_template(
        "dashboard.html",
        statistics=statistics
    )


if __name__ == "__main__":
    app.run(debug=True)