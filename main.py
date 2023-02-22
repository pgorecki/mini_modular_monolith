# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from employee_emodule import  EmployeeModule
from project_module import ProjectModule
from timesheet_module import TimeSheetModule


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    employee_module = EmployeeModule()
    project_module = ProjectModule()
    timesheet_module = TimeSheetModule()

    employee_module.hire_employee(
        employee_id="em1",
        employee_name="Stefan",
        role="python_developer",
        seniority="regular",
    )

    project_module.add_project(project_id="p1", project_name="Foobar")

    try:
        timesheet_module.log_time(project_id="p1", employee_id="em1", minutes=60, description="writing code")
    except AssertionError:
        ...

    project_module.add_member_to_project(project_id="p1", employee_id="em1", role="backend_developer")
    assert project_module.get_project("p1").is_member("em1")

    # TODO: how to guarantee access to project within a timesheet module (if member)
    timesheet_module.log_time(project_id="p1", employee_id="em1", minutes=60, description="writing code")

    employee_module.fire_employee(employee_id="em1")

    report = project_module.get_time_report_for_project(project_id="p1")

    print(report)
