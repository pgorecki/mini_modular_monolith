from dataclasses import dataclass, field
from datetime import date


@dataclass
class ProjectMember:
    employee_id: str
    name: str
    role: str
    start_date: date
    end_date: date
    fte_percent: float


@dataclass
class Project:
    id: str
    client_id: str
    name: str
    members: list[ProjectMember]
    is_public = False


@dataclass
class ProjectModule:

    def get_project(self, project_id):
        ...

    def get_time_report_for_project(self, project_id):
        ...

    def get_all_projects_of_employee(self, employee_id):
        ...

    def add_project(self, project_id, project_name):
        ...

    def change_project_name(self, project_id, new_name):
        ...

    def start_project(self, project_id):
        ...

    def end_project(self, project_id, end_date):
        ...

    def add_member_to_project(self, project_id, employee_id, role):
        ...

    def remove_member_from_project(self, project_id, employee_id):
        ...
