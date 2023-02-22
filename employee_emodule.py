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

    def add_engagement(self, engagement: WorkEngagement):
        self.engagements.append(engagement)

    def end_current_engagement(self):
        self.engagements[-1].end_date = date.today()

@dataclass
class EmployeeModule:
    employees: set[Employee] = field(default_factory=list)

    def hire_employee(self, employee_id, employee_name, role, seniority):
        engagement = WorkEngagement(
            role=role,
            seniority=seniority,
            start_date=date.today(),
            end_date=None
        )
        employee = Employee(
            id=employee_id,
            name=employee_name,
        )
        employee.add_engagement(engagement)

        self.employees.append(employee)

    def fire_employee(self, employee_id):
        for employee in self.employees[:]:
            if employee.id == employee_id:
                employee.end_current_engagement()
                self.employees.remove(employee)
                break
