import unittest
from ex05 import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(1)
        self.r2 = Rectangle(1)
        self.r3 = Rectangle(3)
        self.r4 = Rectangle(2, 1)

    def test_sum_rects(self):
        self.assertEqual(self.r1 + self.r2, self.r4)

    def test_sub_rects(self):
        self.assertEqual(self.r4 - self.r2, self.r1)

    def test_create_rect_with_negative_sides(self):
        with self.assertRaises(ValueError):
            Rectangle(-1)

    def test_is_sum_rectangle(self):
        self.assertIsInstance(self.r1 + self.r2, Rectangle)

    def test_is_sub_rectangle(self):
        self.assertIsInstance(self.r4 - self.r2, Rectangle)

    def test_calculate_rect_area(self):
        self.assertEqual(self.r1.get_square(), 1)
        self.assertEqual(self.r4.get_square(), 2)


if __name__ == "__main__":
    unittest.main(verbosity=4)
