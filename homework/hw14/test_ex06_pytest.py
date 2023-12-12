import pytest
from ex06 import Employee


@pytest.fixture
def emp():
    return Employee('Ivanov', 'Ivan', 'Ivanovich',
                    30, 'manager', 50000)


def test_employee_full_name(emp):
    assert emp.full_name() == "Ivanov Ivan Ivanovich"


def test_employee_birthday(emp):
    emp.birthday()
    assert emp.get_age() == 31


def test_employee_raise_salary(emp):
    emp.raise_salary(10)
    assert emp.salary == 55000.0


def test_employee_str(emp):
    assert emp.__str__() == "Ivanov Ivan Ivanovich (Manager)"


def test_employee_last_name_title():
    emp = Employee('ivanov', 'ivan', 'ivanovich',
                   30, 'manager', 50000)
    assert emp.last_name == "Ivanov"
