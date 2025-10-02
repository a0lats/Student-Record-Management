# Author: Adeoluwa (Ade) Olateru-Olagbegi
# Project: Student Record Management System
# Date: 07/21/2025
# Description: A simple Python + SQLite program to manage student records
# with full CRUD (Create, Read, Update, Delete) operations and persistent storage.

import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT
)
""")
conn.commit()

# CRUD Functions
def add_student(name, age, major):
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    conn.commit()

def view_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def update_student(student_id, name=None, age=None, major=None):
    if name:
        cursor.execute("UPDATE students SET name=? WHERE id=?", (name, student_id))
    if age:
        cursor.execute("UPDATE students SET age=? WHERE id=?", (age, student_id))
    if major:
        cursor.execute("UPDATE students SET major=? WHERE id=?", (major, student_id))
    conn.commit()

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
add_student("John Doe", 19, "Information Systems")
add_student("Sarah Lee", 23, "Data Science")

print("All Students:", view_students())

update_student(1, age=20)

delete_student(2)

print("Updated Students:", view_students())
