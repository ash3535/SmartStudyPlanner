from database import get_connection


class TaskManager:

    def add_task(self, task):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO study_tasks
            (title, subject, difficulty, estimated_hours, deadline, priority)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            task.title,
            task.subject,
            task.difficulty,
            task.estimated_hours,
            task.deadline,
            task.priority
        ))

        connection.commit()

        cursor.close()
        connection.close()

    def get_tasks(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, title, subject, difficulty,
                   estimated_hours, deadline, priority
            FROM study_tasks
            ORDER BY id
        """)

        tasks = cursor.fetchall()

        cursor.close()
        connection.close()

        return tasks

    def update_task(
            self,
            task_id,
            title,
            subject,
            difficulty,
            estimated_hours,
            deadline,
            priority
        ):
            connection = get_connection()
            cursor = connection.cursor()
    
            query = """
                UPDATE study_tasks
                SET title = %s,
                    subject = %s,
                    difficulty = %s,
                    estimated_hours = %s,
                    deadline = %s,
                    priority = %s
                WHERE id = %s
            """
    
            cursor.execute(query, (
                title,
                subject,
                difficulty,
                estimated_hours,
                deadline,
                priority,
                task_id
            ))
    
            connection.commit()
    
            cursor.close()
            connection.close()

    def delete_task(self, task_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM study_tasks WHERE id = %s",
            (task_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()