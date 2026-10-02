from database import get_connection
from werkzeug.security import generate_password_hash, check_password_hash


class UserManager:

    def create_user(self, username, email, password):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id
            FROM users
            WHERE username = %s OR email = %s
        """, (username, email))

        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            connection.close()
            return False

        password_hash = generate_password_hash(password)

        cursor.execute("""
            INSERT INTO users
            (username, email, password_hash)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (username, email, password_hash))

        user_id = cursor.fetchone()[0]

        connection.commit()

        cursor.close()
        connection.close()

        return user_id

    def authenticate_user(self, username_or_email, password):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, username, email, password_hash
            FROM users
            WHERE username = %s OR email = %s
        """, (username_or_email, username_or_email))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user and check_password_hash(user[3], password):
            return user

        return None