from dataclasses import dataclass, field
from collections import defaultdict
from functools import partial
from messaging import event_handler
from project_module import NewProjectWasCreated, MemberWasAddedToProject
from employee_emodule import EmployeeWasFired


@dataclass
class TimeEntry:
    project_id: str
    employee_id: str
    minutes: int
    description: str


@dataclass
class TimeSheetModule:
    time_entries: list[TimeEntry] = field(default_factory=list)
    project_access: dict[str, set] = field(default_factory=partial(defaultdict, set))

    def has_access_to_project(self, employee_id, project_id):
        return project_id in self.project_access.get(employee_id, [])

    def grant_access_to_project(self, employee_id, project_id):
        self.project_access[employee_id].add(project_id)

    def revoke_access_to_project(self, employee_id, project_id):
        self.project_access[employee_id].discard(project_id)

    def log_time(self, employee_id, project_id, minutes, description):
        assert self.has_access_to_project(employee_id=employee_id, project_id=project_id)
        entry = TimeEntry(
            project_id=project_id,
            employee_id=employee_id,
            minutes=minutes,
            description=description)
        self.time_entries.append(entry)

    @event_handler(MemberWasAddedToProject)
    def grant_access_to_project_policy(self, event: MemberWasAddedToProject):
        self.grant_access_to_project(employee_id=event.employee_id, project_id=event.project_id)

    @event_handler(EmployeeWasFired)
    def when_employee_is_fired_revoke_access_to_all_projects_policy(self, event: EmployeeWasFired):
        del self.project_access[event.employee_id]