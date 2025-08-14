from fastapi import FastAPI

data = [
    {
        "id": 1,
        "name": "John Doe",
        "gender": "M",
        "salary": 1000,
        "address": "123 Street",
    },
    {
        "id": 2,
        "name": "Eliza Dahm",
        "gender": "F",
        "salary": 2000,
        "address": "456 Avenue",
    },
    {
        "id": 3,
        "name": "Mauro Coimbra",
        "gender": "M",
        "salary": 0,
        "address": "789 House",
    },
]

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/employees")
def get_all():
    return data

@app.get("/employees/{employee_id}")
def get_employee_path(employee_id: str):
    employee_id = int(employee_id)

    for employee in data:
        if employee["id"]== employee_id:
            return employee

    return {"message": "Employee not found"}

@app.get("/employees/")
def get_employee_query(employee_id: str):
    employee_id = int(employee_id)

    for employee in data:
        if employee["id"]== employee_id:
            return employee

    return {"message": "Employee not found"}

@app.post("/employees")
def create_employee(employee: dict):
    new_employee_id = max(employee["id"] for employee in data) + 1

    new_employee = {
        "id": new_employee_id,
        "name": employee["name"],
        "gender": employee["gender"],
        "salary": employee["salary"],
        "address": employee["address"],
    }
    data.append(new_employee)
    
    return {
        "message": "Employee created",
        "employee": new_employee,
    }

@app.put("/employees/{employee_id}")
def update_employee(employee_id: str):
    pass

@app.delete("employees/{employee_id}")
def delete_employee(employee_id: str):
    pass