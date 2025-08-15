from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

class Gender(str, Enum):
    M = "M"
    F = "F"

class EmployeeBase(BaseModel):
    name: str = Field(..., max_length=64, description="Name of the employee")
    gender: Gender = Field(default=None, description="Gender of the employee")
    salary: float = Field(..., description="Salary of the employee")
    address: str = Field(..., max_length=128, description="Description of the employee")

class Employee(EmployeeBase):
    id: int = Field(..., description="ID of the employee")

class EmployeeCreate(EmployeeBase):
    pass
    

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=64, description="Name of the employee")
    gender: Optional[Gender] = Field(default=None, description="Gender of the employee")
    salary: Optional[float] = Field(None, description="Salary of the employee")
    address: Optional[str] = Field(None, max_length=128, description="Description of the employee")