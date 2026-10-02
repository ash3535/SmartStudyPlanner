class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def update_task(self, index, title, subject, difficulty, estimated_hours, deadline, priority):
        task = self.tasks[index]

        task.title = title
        task.subject = subject
        task.difficulty = difficulty
        task.estimated_hours = estimated_hours
        task.deadline = deadline
        task.priority = priority

    def delete_task(self, index):
        self.tasks.pop(index)