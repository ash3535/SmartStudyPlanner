import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="smart_study_planner",
        user="postgres",
        password="ash345",
        port="5432"
    )