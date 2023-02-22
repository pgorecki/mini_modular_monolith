from dataclasses import dataclass, field
from collections import defaultdict
from functools import partial

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