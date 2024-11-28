import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",          # Replace with your host if not localhost
        user="root",               # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="RegistrationDB"  # The database you created
    )
