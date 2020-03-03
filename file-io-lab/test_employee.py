#!/usr/bin/env python3.7

from employee import Employee

file_name = "test_employee_file.txt"

with open(file_name, "w") as f:
    f.writelines(
        [
            "Kevin Bacon,kbacon@example.com,CEO,555-867-5309\n",
            "Bruce Wayne,bwayne@example.com,President,\n",
        ]
    )

employees = Employee.get_all(file_name)

assert len(employees) == 2, f"Expected 2 employees, but got {len(employees)}"

assert (
    Employee.get_at_line(1, file_name).__dict__ == employees[0].__dict__
), f"Expected Employee.get_at_line(1) to return {employees[0].__dict__} but got {Employee.get_at_line(1, file_name).__dict__}"

cmo = Employee("Betty White", "bwhite@example.com", "CMO")
cmo.save(file_name)

assert (
    len(Employee.get_all(file_name)) == 3
), f"Expected 3 employees, but got {len(Employee.get_all(file_name))}"

president = employees[1]

president.phone_number = "555-555-5555"
president.save(file_name)

new_president = Employee.get_at_line(president.identifier, file_name)

assert (
    new_president.phone_number == "555-555-5555"
), f"Expected phone number to be 555-555-5555, but got {new_president.phone_number}"

