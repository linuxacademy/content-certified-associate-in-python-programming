#!/usr/bin/env python3.7

from os import remove
from employee import Employee, DatabaseError, MissingEmployeeError

file_name = "test_employee_file.txt"

try:
    remove(file_name)
except:
    pass

try:
    Employee.get_all(file_name)
except Exception as err:
    assert (
        err.__class__ == DatabaseError
    ), f"Expected DatabaseError but got {err.__class__.__name__}"


with open(file_name, "w") as f:
    f.writelines(
        [
            "Kevin Bacon,kbacon@example.com,CEO,555-867-5309\n",
            "Bruce Wayne,bwayne@example.com,President,\n",
        ]
    )

try:
    Employee.get_at_line(3, file_name)
except Exception as err:
    assert (
        err.__class__ == MissingEmployeeError
    ), f"Expected MissingEmployeeError but got {err.__class__.__name__}"

new_employee = Employee("Betty White", "bwhite@example.com", "CMO", identifier=4)

try:
    new_employee.save(file_name)
except Exception as err:
    assert (
        err.__class__ == MissingEmployeeError
    ), f"Expected MissingEmployeeError but got {err.__class__.__name__}"
