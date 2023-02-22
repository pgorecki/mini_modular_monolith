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

    def has_access_to_project(self, employee_id, project_id):
        ...

    def grant_access_to_project(self, employee_id, project_id):
        ...

    def revoke_access_to_project(self, employee_id, project_id):
        ...

    def log_time(self, employee_id, project_id, minutes, description):
        ...