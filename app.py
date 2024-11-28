from flask import Flask, request, jsonify
from db import get_db_connection

import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database',
            user='your_username',
            password='your_password'
        )
        return connection
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None




# Create
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s)"
    values = (data['Name'], data['Email'], data['DateOfBirth'], data['PhoneNumber'], data['Address'])
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    return jsonify({"message": "User registered successfully"}), 200

# Read
@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Registration")
    users = cursor.fetchall()
    connection.close()
    return jsonify(users)

# Update
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "UPDATE Registration SET Name = %s, Email = %s, DateOfBirth = %s, PhoneNumber = %s, Address = %s WHERE ID = %s"
    values = (data['Name'], data['Email'], data['DateOfBirth'], data['PhoneNumber'], data['Address'], id)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    return jsonify({"message": "User updated successfully"})

# Delete
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Registration WHERE ID = %s", (id,))
    connection.commit()
    connection.close()
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

    # Example: Create a new user
    register_user('John Doe', 'john.doe@example.com', '1990-01-01')

    # Example: Read all users
    get_users()

    # Example: Update a user (replace '1' with an actual ID)
    update_user(1, 'Jane Doe', 'jane.doe@example.com', '1991-01-01')

    # Example: Delete a user (replace '1' with an actual ID)
    delete_user(1)
