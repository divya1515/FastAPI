from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def index():
    return {"name":"First Data"}

students={
    1:{
        "name":"john",
        "rollno":"1234"
    }
}

@app.get("/get-student/{student_id}")
def get_student(student_id:int=Path(...,description="The ID of the student you want to view",gt=0,lt=3)):
    return students[student_id]
# student_id must be int and some more conditions tobe applied on student_id is defined in Path  ... indicates that it is required , and no default value can be given to this id , and description is given for id , id must be greater than 0 (gt=0) and less than 3(lt=3)

class Student(BaseModel):
    name:str
    rollno:str

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int,name:Optional[str]=None,):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}  

@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {"Error":"Student-exists"}
    students[student_id]=student
    return students[student_id]