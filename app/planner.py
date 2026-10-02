from datetime import date


def calculate_score(task):
    task_id, title, subject, difficulty, hours, deadline, priority = task

    today = date.today()
    days_left = (deadline - today).days

    # Deadline score
    if days_left <= 1:
        deadline_score = 10
    elif days_left <= 3:
        deadline_score = 7
    elif days_left <= 7:
        deadline_score = 4
    else:
        deadline_score = 1

    # Priority score
    priority_scores = {
        "High": 10,
        "Medium": 5,
        "Low": 2
    }

    priority_score = priority_scores.get(priority, 2)

    # Difficulty score
    difficulty_scores = {
        "Hard": 6,
        "Medium": 4,
        "Easy": 2
    }

    difficulty_score = difficulty_scores.get(difficulty, 2)

    # Longer tasks get slightly higher priority
    hours_score = min(float(hours), 10)

    total_score = (
        deadline_score
        + priority_score
        + difficulty_score
        + hours_score
    )

    return total_score


def create_study_plan(tasks):
    return sorted(
        tasks,
        key=calculate_score,
        reverse=True
    )