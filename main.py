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

@app.get("/employees/{input_employee_id}")
def get_employee_path(input_employee_id: str):
    input_employee_id = int(input_employee_id)

    for employee in data:
        if employee["id"] == input_employee_id:
            return employee

    return {"message": "Employee not found"}

@app.get("/employees/")
def get_employee_query(input_employee_id: str):
    input_employee_id = int(input_employee_id)

    for employee in data:
        if employee["id"] == input_employee_id:
            return employee

    return {"message": "Employee not found"}

@app.post("/employees")
def create_employee(input_employee: dict):
    new_employee_id = max(employee["id"] for employee in data) + 1

    new_employee = {
        "id": new_employee_id,
        "name": input_employee["name"],
        "gender": input_employee["gender"],
        "salary": input_employee["salary"],
        "address": input_employee["address"],
    }
    data.append(new_employee)
    
    return {
        "message": "Employee created",
        "employee": new_employee,
    }

@app.put("/employees/{input_employee_id}")
def update_employee(input_employee_id: str, input_employee: dict):
    input_employee_id = int(input_employee_id)

    updated_index = None
    for index, employee in enumerate(data):
        if employee["id"] == input_employee_id:
            updated_index = index
            break

    if updated_index == None:
        return {"message": "Employee not found"}
    
    updated_employee = {
        "id": input_employee_id,
        "name": input_employee.get("name", data[updated_index]["name"]),
        "gender": input_employee.get("gender", data[updated_index]["gender"]),
        "salary": input_employee.get("salary", data[updated_index]["salary"]),
        "address": input_employee.get("address", data[updated_index]["address"]),
    }

    data[updated_index] = updated_employee

    return {
        "message": "Employee updated",
        "updated_fields": input_employee,
    }
    

@app.delete("/employees/{input_employee_id}")
def delete_employee(input_employee_id: str):
    input_employee_id = int(input_employee_id)

    for index, employee in enumerate(data):
        if input_employee_id == employee["id"]:
            removed_employee = data.pop(index)
            return {
                "message": "Successfully removed employee",
                "employee": removed_employee
            }

    return {"message": "Employee not found"}