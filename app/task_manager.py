from database import get_connection


class TaskManager:

    def add_task(self, task, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO study_tasks
            (title, subject, difficulty, estimated_hours,
             deadline, priority, user_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            task.title,
            task.subject,
            task.difficulty,
            task.estimated_hours,
            task.deadline,
            task.priority,
            user_id
        ))

        connection.commit()

        cursor.close()
        connection.close()


    def get_tasks(self, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, title, subject, difficulty,
                   estimated_hours, deadline, priority, completed
            FROM study_tasks
            WHERE user_id = %s
            ORDER BY completed ASC, id
        """, (user_id,))

        tasks = cursor.fetchall()

        cursor.close()
        connection.close()

        return tasks


    def update_task(
        self,
        task_id,
        user_id,
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
              AND user_id = %s
        """

        cursor.execute(query, (
            title,
            subject,
            difficulty,
            estimated_hours,
            deadline,
            priority,
            task_id,
            user_id
        ))

        connection.commit()

        cursor.close()
        connection.close()


    def delete_task(self, task_id, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM study_tasks
            WHERE id = %s
              AND user_id = %s
        """, (task_id, user_id))

        connection.commit()

        cursor.close()
        connection.close()


    def get_statistics(self, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) AS total_tasks,
                COALESCE(SUM(estimated_hours), 0) AS total_hours,
                COUNT(*) FILTER (WHERE priority = 'High') AS high_priority,
                COUNT(*) FILTER (WHERE completed = TRUE) AS completed_tasks,
                COUNT(*) FILTER (WHERE completed = FALSE) AS pending_tasks
            FROM study_tasks
            WHERE user_id = %s
        """, (user_id,))

        statistics = cursor.fetchone()

        cursor.close()
        connection.close()

        return statistics


    def toggle_task(self, task_id, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE study_tasks
            SET completed = NOT completed
            WHERE id = %s
              AND user_id = %s
        """, (task_id, user_id))

        connection.commit()

        cursor.close()
        connection.close()