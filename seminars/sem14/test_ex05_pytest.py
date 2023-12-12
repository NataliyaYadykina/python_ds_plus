import pytest
from ex05 import Rectangle


@pytest.fixture
def r1():
    return Rectangle(1)


@pytest.fixture
def r2():
    return Rectangle(1)


@pytest.fixture
def r3():
    return Rectangle(3)


@pytest.fixture
def r4():
    return Rectangle(2, 1)


def test_sum_rects(r1, r2, r4):
    assert r1 + r2 == r4


def test_sub_rects(r1, r2, r4):
    assert r4 - r2 == r1


def test_create_rect_with_negative_sides():
    with pytest.raises(ValueError):
        Rectangle(-1)


def test_is_sum_rectangle(r1, r2):
    assert isinstance(r1 + r2, Rectangle)


def test_is_sub_rectangle(r4, r2):
    assert isinstance(r4 - r2, Rectangle)


def test_calculate_rect_area(r1, r4):
    assert r1.get_square() == 1
    assert r4.get_square() == 2
