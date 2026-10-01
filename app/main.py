from models import StudyTask


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


tasks = [task1, task2]


for task in tasks:
    print(task)