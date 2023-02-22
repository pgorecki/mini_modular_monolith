from dataclasses import dataclass, field
from datetime import date

@dataclass
class WorkEngagement:
    role: str
    seniority: str
    start_date: date
    end_date: date = None


@dataclass
class Employee:
    id: str
    name: str
    engagements: list[WorkEngagement] = field(default_factory=list)


@dataclass
class EmployeeModule:
    employees: set[Employee] = field(default_factory=list)

    def hire_employee(self, employee_id, employee_name, role, seniority):
        ...

    def fire_employee(self, employee_id):
        ...