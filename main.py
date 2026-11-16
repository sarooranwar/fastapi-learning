from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Aisha Khan", "age": 20, "course": "Computer Science"},
    {"id": 2, "name": "Rahul Sharma", "age": 21, "course": "Mathematics"},
    {"id": 3, "name": "Priya Patel", "age": 19, "course": "Physics"},
]

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "koi student nahi hai"}
