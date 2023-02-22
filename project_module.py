from dataclasses import dataclass, field
from datetime import date
from messaging import EventBase, command_handler, event_handler
from employee_emodule import EmployeeWasFired

@dataclass
class NewProjectWasCreated(EventBase):
    project_id: str
    project_name: str


@dataclass
class MemberWasAddedToProject(EventBase):
    employee_id: str
    project_id: str


@dataclass
class MemberWasRemovedFromProject(EventBase):
    employee_id: str
    project_id: str


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
    members: list[ProjectMember] = field(default_factory=list)
    is_public = False

    def is_member(self, employee_id):
        return any([m.employee_id == employee_id for m in self.members])

    def add_member(self, employee_id, role, fte_percent=1):
        membership = ProjectMember(
            employee_id=employee_id,
            name=...,
            role=role,
            start_date=date.today(),
            end_date=None,
            fte_percent=fte_percent,
        )
        self.members.append(membership)

    def remove_member(self, employee_id):
        for member in self.members[:]:
            if member.employee_id == employee_id:
                self.members.remove(member)
                break


@dataclass
class ProjectModule:
    projects: dict[str, Project] = field(default_factory=dict)

    def get_project(self, project_id):
        return self.projects[project_id]

    def get_time_report_for_project(self, project_id):
        project = self.get_project(project_id)
        report = [
            ('Team member', 'total time'),
        ]
        return report

    def get_all_projects_of_employee(self, employee_id):
        return []

    @command_handler
    def add_project(self, project_id, project_name):
        new_project = Project(
            id=project_id,
            client_id=...,
            name=project_name,
        )
        self.projects[project_id] = new_project
        return NewProjectWasCreated(project_id=project_id, project_name=project_name)

    def change_project_name(self, project_id, new_name):
        project = self.get_project(project_id)
        project.name = new_name

    def start_project(self, project_id):
        ...

    def end_project(self, project_id, end_date):
        ...

    @command_handler
    def add_member_to_project(self, project_id, employee_id, role):
        project = self.get_project(project_id)
        project.add_member(employee_id, role)
        return MemberWasAddedToProject(employee_id=employee_id, project_id=project_id)

    def remove_member_from_project(self, project_id, employee_id):
        project = self.get_project(project_id)
        project.remove_member(employee_id)
        return MemberWasRemovedFromProject(employee_id=employee_id, project_id=project_id)

    @event_handler(EmployeeWasFired)
    def if_employee_was_fired_then_remove_from_all_projects_policy(self, event: EmployeeWasFired):
        projects = self.get_all_projects_of_employee(event.employee_id)
        for project in projects:
            # TODO: this is a command that may result in new events to be fired...
            self.remove_member_from_project(project_id=project.id, employee_id=event.employee_id)