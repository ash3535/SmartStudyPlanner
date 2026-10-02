from flask import Flask, render_template, request, redirect, flash

from models import StudyTask
from task_manager import TaskManager
from planner import create_study_plan


app = Flask(__name__)

app.secret_key = "smart-study-planner-secret-key"

manager = TaskManager()


@app.route("/")
def home():

    tasks = manager.get_tasks()

    return render_template(
        "index.html",
        tasks=tasks
    )


@app.route("/add", methods=["POST"])
def add_task():

    try:

        title = request.form.get("title", "").strip()
        subject = request.form.get("subject", "").strip()
        difficulty = request.form.get("difficulty", "")
        estimated_hours = float(
            request.form.get("estimated_hours", 0)
        )
        deadline = request.form.get("deadline", "")
        priority = request.form.get("priority", "")

        # Validate text fields
        if not title or not subject or not deadline:
            flash("Please fill in all required fields.", "error")
            return redirect("/")

        # Validate hours
        if estimated_hours <= 0:
            flash("Study hours must be greater than 0.", "error")
            return redirect("/")

        # Validate difficulty
        if difficulty not in ["Easy", "Medium", "Hard"]:
            flash("Invalid difficulty selected.", "error")
            return redirect("/")

        # Validate priority
        if priority not in ["Low", "Medium", "High"]:
            flash("Invalid priority selected.", "error")
            return redirect("/")

        task = StudyTask(
            title,
            subject,
            difficulty,
            estimated_hours,
            deadline,
            priority
        )

        manager.add_task(task)

        flash("Task added successfully!", "success")

    except ValueError:
        flash("Please enter a valid number for study hours.", "error")

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    manager.delete_task(task_id)

    flash("Task deleted.", "success")

    return redirect("/")


@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):

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
            flash("Please fill in all required fields.", "error")
            return redirect("/")

        if estimated_hours <= 0:
            flash("Study hours must be greater than 0.", "error")
            return redirect("/")

        if difficulty not in ["Easy", "Medium", "Hard"]:
            flash("Invalid difficulty selected.", "error")
            return redirect("/")

        if priority not in ["Low", "Medium", "High"]:
            flash("Invalid priority selected.", "error")
            return redirect("/")

        manager.update_task(
            task_id,
            title,
            subject,
            difficulty,
            estimated_hours,
            deadline,
            priority
        )

        flash("Task updated successfully!", "success")

    except ValueError:
        flash("Please enter a valid number for study hours.", "error")

    return redirect("/")


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):

    manager.toggle_task(task_id)

    return redirect("/")


@app.route("/plan")
def study_plan():

    tasks = manager.get_tasks()

    planned_tasks = create_study_plan(tasks)

    return render_template(
        "plan.html",
        tasks=planned_tasks
    )


@app.route("/dashboard")
def dashboard():

    statistics = manager.get_statistics()

    return render_template(
        "dashboard.html",
        statistics=statistics
    )


if __name__ == "__main__":
    app.run(debug=True)