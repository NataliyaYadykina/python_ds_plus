import unittest
from ex04 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp = Employee('Ivanov', 'Ivan', 'Ivanovich',
                            30, 'manager', 50000)

    def test_employee_full_name(self):
        self.assertEqual(self.emp.full_name(), "Ivanov Ivan Ivanovich")

    def test_employee_birthday(self):
        self.emp.birthday()
        self.assertEqual(self.emp.get_age(), 31)

    def test_employee_raise_salary(self):
        self.emp.raise_salary(10)
        self.assertEqual(self.emp.salary, 55000.0)

    def test_employee_str(self):
        self.assertEqual(self.emp.__str__(),
                         "Ivanov Ivan Ivanovich (Manager)")

    def test_employee_last_name_title(self):
        self.emp = Employee('ivanov', 'ivan', 'ivanovich',
                            30, 'manager', 50000)
        self.assertNotEqual(self.emp.last_name, "Ivan")


if __name__ == "__main__":
    unittest.main(verbosity=4)
