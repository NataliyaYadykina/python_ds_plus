import pytest
from ex05 import Rectangle, NegativeValueError


def test_width():
    r1 = Rectangle(5)
    assert r1.width == 5


def test_height():
    r2 = Rectangle(3, 4)
    assert r2.height == 4


def test_perimeter():
    r1 = Rectangle(5)
    assert r1.perimeter() == 20


def test_area():
    r2 = Rectangle(3, 4)
    assert r2.area() == 12


def test_subtraction():
    r1 = Rectangle(10, 3)
    r2 = Rectangle(1, 4)
    assert r1 - r2 == Rectangle(9, 1)


def test_addition():
    r1 = Rectangle(5, 3)
    r2 = Rectangle(1, 4)
    r3 = r1 + r2
    assert r3.width == 6
    assert r3.height == 7.0


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)


def test_set_width():
    r1 = Rectangle(5)
    r1.width = 10
    assert r1.width == 10


def test_set_negative_width():
    r1 = Rectangle(5)
    with pytest.raises(NegativeValueError):
        r1.width = -10


def test_set_height():
    r2 = Rectangle(3, 4)
    r2.height = 6
    assert r2.height == 6


def test_set_negative_height():
    r2 = Rectangle(3, 4)
    with pytest.raises(NegativeValueError):
        r2.height = -6


def test_subtraction_negative_result():
    r1 = Rectangle(3, 10)
    r2 = Rectangle(4, 1)
    with pytest.raises(NegativeValueError):
        r1 - r2


def test_subtraction_same_perimeter():
    r1 = Rectangle(5, 4)
    r2 = Rectangle(1, 3)
    assert r1 - r2 == Rectangle(4, 1.0)
