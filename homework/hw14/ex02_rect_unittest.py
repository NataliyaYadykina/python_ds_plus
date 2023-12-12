import unittest
from ex02 import Rectangle, NegativeValueError


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(3, 4)
        self.r3 = Rectangle(8, 9.0)
        self.r4 = Rectangle(7, 6.0)

    def test_width(self):
        self.assertEqual(self.r1.width, 5)

    def test_height(self):
        self.assertEqual(self.r2.height, 4)

    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter(), 20)

    def test_area(self):
        self.assertEqual(self.r2.area(), 12)

    def test_addition(self):
        self.assertEqual(self.r1 + self.r2, self.r3)

    def test_subtraction(self):
        r1 = Rectangle(10)
        self.assertEqual(r1 - self.r2, self.r4)

    def test_negative_width(self):
        with self.assertRaises(NegativeValueError):
            Rectangle(-5)

    def test_negative_height(self):
        with self.assertRaises(NegativeValueError):
            Rectangle(5, -4)

    def test_set_width(self):
        self.r1.width = 10
        self.assertEqual(self.r1.width, 10)

    def test_set_negative_width(self):
        with self.assertRaises(NegativeValueError):
            self.r1.width = -10

    def test_set_height(self):
        self.r2.height = 6
        self.assertEqual(self.r2.height, 6)

    def test_set_negative_height(self):
        with self.assertRaises(NegativeValueError):
            self.r2.height = -6

    def test_subtraction_negative_result(self):
        self.r1 = Rectangle(3, 4)
        self.r2 = Rectangle(10)
        with self.assertRaises(NegativeValueError):
            self.r1 - self.r2

    def test_subtraction_same_perimeter(self):
        self.r2 = Rectangle(4, 3)
        self.assertEqual(self.r1 - self.r2, Rectangle(1, 1.0))

    # def test_is_sum_rectangle(self):
    #     self.assertIsInstance(self.r1 + self.r2, Rectangle)

    # def test_is_sub_rectangle(self):
    #     self.assertIsInstance(self.r4 - self.r2, Rectangle)

    # def test_calculate_rect_area(self):
    #     self.assertEqual(self.r1.get_square(), 1)
    #     self.assertEqual(self.r4.get_square(), 2)


if __name__ == "__main__":
    unittest.main(verbosity=4)
