class StudyTask:
    
    def __init__(
        self,
        title,
        subject,
        difficulty,
        estimated_hours,
        deadline,
        priority
    ):
        
        if estimated_hours <= 0:
            raise ValueError("Estimated hours must be greater than 0")
        
        self.title = title
        self.subject = subject
        self.difficulty = difficulty
        self.estimated_hours = estimated_hours
        self.deadline = deadline
        self.priority = priority

    def __str__(self):
        return f"{self.title} | {self.subject} | {self.difficulty} | {self.estimated_hours} hrs | {self.deadline} | {self.priority}"