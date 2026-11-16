from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = [
    {"id": 1, "name": "Aisha Khan", "age": 20, "course": "Computer Science"},
    {"id": 2, "name": "Rahul Sharma", "age": 21, "course": "Mathematics"},
    {"id": 3, "name": "Priya Patel", "age": 19, "course": "Physics"},
]
class Student(BaseModel):
    name: str
    age: int
    course: str

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "koi student nahi hai"}

@app.post("/students")
def add_student(student: Student):
    new_student = {"id": len(students) + 1, **student.model_dump()}
    students.append(new_student)
    return new_student
