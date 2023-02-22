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
    projects: dict[str, Project] = field(default_factory=dict)

    def get_project(self, project_id):
        return self.projects[project_id]

    def get_time_report_for_project(self, project_id):
        project = self.get_project(project_id)
        report = [
            ('Team member', 'total time'),
            ...
        ]
        return report

    def get_all_projects_of_employee(self, employee_id):
        ...

    def add_project(self, project_id, project_name):
        new_project = Project()
        self.projects[project_id] = new_project

    def change_project_name(self, project_id, new_name):
        project = self.get_project(project_id)
        project.name = new_name

    def start_project(self, project_id):
        ...

    def end_project(self, project_id, end_date):
        ...

    def add_member_to_project(self, project_id, employee_id, role):
        ...

    def remove_member_from_project(self, project_id, employee_id):
        ...
