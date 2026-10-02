from models import StudyTask
from task_manager import TaskManager

manager = TaskManager()

task1 = StudyTask(
    "Learn SQL Joins",
    "PostgreSQL",
    "Easy",
    2,
    "2026-10-05",
    "High"
)

task2 = StudyTask(
    "Practice Recursion",
    "Python",
    "Medium",
    3,
    "2026-10-07",
    "High"
)

manager.add_task(task1)
manager.add_task(task2)

print("=== ALL TASKS ===")

for task in manager.get_tasks():
    print(task)

print("\n=== UPDATE TASK ===")

manager.update_task(
    0,
    "Learn Advanced SQL Joins",
    "PostgreSQL",
    "Medium",
    4,
    "2026-10-06",
    "High"
)

print(manager.get_tasks()[0])

print("\n=== DELETE TASK ===")

manager.delete_task(1)

for task in manager.get_tasks():
    print(task)