from typing import List
from fastapi import FastAPI, HTTPException

from models.employee import (
    Employee,
    EmployeeCreate,
    EmployeeUpdate,
)

data = [
    Employee(
        id=1,
        name="John Doe",
        gender="M",
        salary=1000,
        address="123 Street"
    ),
    Employee(
        id=2,
        name="Eliza Dahm",
        gender="F",
        salary=2000,
        address="456 Avenue"
    ),
    Employee(
        id=3,
        name="Mauro Coimbra",
        gender="M",
        salary=0,
        address="789 House"
    ),
]

app = FastAPI()

@app.get("/employees", response_model=List[Employee])
def get_all():
    return data

@app.get("/employees/{input_employee_id}", response_model=Employee)
def get_employee_path(input_employee_id: str):
    input_employee_id = int(input_employee_id)

    for employee in data:
        if employee.id == input_employee_id:
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")

@app.get("/employees/", response_model=Employee)
def get_employee_query(input_employee_id: str):
    input_employee_id = int(input_employee_id)

    for employee in data:
        if employee.id == input_employee_id:
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees", response_model=Employee)
def create_employee(input_employee: EmployeeCreate):
    new_employee_id = max(employee.id for employee in data) + 1

    new_employee = Employee(
        id=new_employee_id,
        name=input_employee.name,
        gender=input_employee.gender,
        salary=input_employee.salary,
        address=input_employee.address,
    )
    data.append(new_employee)
    
    return new_employee

@app.put("/employees/{input_employee_id}", response_model=Employee)
def update_employee(input_employee_id: str, input_employee: EmployeeUpdate):
    input_employee_id = int(input_employee_id)

    updated_index = None
    for index, employee in enumerate(data):
        if employee.id == input_employee_id:
            updated_index = index
            break

    if updated_index == None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    updated_employee = Employee(
        id=input_employee_id,
        name=input_employee.name if input_employee.name is not None else data[updated_index].name,
        gender=input_employee.gender if input_employee.gender is not None else data[updated_index].gender,
        salary=input_employee.salary if input_employee.salary is not None else data[updated_index].salary,
        address=input_employee.address if input_employee.address is not None else data[updated_index].address,
    )

    data[updated_index] = updated_employee

    return updated_employee
    

@app.delete("/employees/{input_employee_id}", response_model=Employee)
def delete_employee(input_employee_id: str):
    input_employee_id = int(input_employee_id)

    for index, employee in enumerate(data):
        if input_employee_id == employee.id:
            removed_employee = data.pop(index)
            return removed_employee

    raise HTTPException(status_code=404, detail="Employee not found")