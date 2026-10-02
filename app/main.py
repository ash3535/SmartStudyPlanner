from flask import Flask, render_template, request, redirect

from models import StudyTask
from task_manager import TaskManager
from planner import create_study_plan


app = Flask(__name__)

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

    title = request.form["title"]
    subject = request.form["subject"]
    difficulty = request.form["difficulty"]
    estimated_hours = float(request.form["estimated_hours"])
    deadline = request.form["deadline"]
    priority = request.form["priority"]

    task = StudyTask(
        title,
        subject,
        difficulty,
        estimated_hours,
        deadline,
        priority
    )

    manager.add_task(task)

    return redirect("/")


@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):

    title = request.form["title"]
    subject = request.form["subject"]
    difficulty = request.form["difficulty"]
    estimated_hours = float(request.form["estimated_hours"])
    deadline = request.form["deadline"]
    priority = request.form["priority"]

    manager.update_task(
        task_id,
        title,
        subject,
        difficulty,
        estimated_hours,
        deadline,
        priority
    )

    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    manager.delete_task(task_id)

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