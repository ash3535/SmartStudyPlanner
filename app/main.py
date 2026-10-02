from task_manager import TaskManager

manager = TaskManager()

manager.update_task(
    1,
    "Learn Advanced SQL Joins",
    "PostgreSQL",
    "Medium",
    4,
    "2026-10-06",
    "High"
)

print("Task updated successfully!")

for task in manager.get_tasks():
    print(task)