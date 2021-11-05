from src.Geometry import Point
import pytest


def test_instantiation():
    point = Point(4, 5.5)
    assert isinstance(point, Point)
    assert point.x == 4
    assert point.y == 5.5


def test_coord_type():
    """Check we get an error if one of the coordinates is not float or int """
    with pytest.raises(AssertionError):
        point = Point([0], 1)


def test_is_lower():
    """Test is_lower method """
    p1 = Point(1, 2)
    p2 = Point(2, 4.2)
    assert p1.is_lower(p2)


def test_is_lower_if_equal():
    """Test is_lower is True if the two points are the same """
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    assert p1.is_lower(p2)


def test_is_not_lower():
    """Test is_lower is False on two 'not comparable' points"""
    p1 = Point(1, 2)
    p2 = Point(0.9, 5)
    assert not p1.is_lower(p2)


def test_is_not_equal():
    """Test is equal is False with different points """
    p1 = Point(1, 2)
    p2 = Point(1, 3)
    assert not p1.is_equal(p2)


def test_is_equal():
    """Test is equal is True, with 'equal' coordinates of different types """
    p1 = Point(1, 2)
    p2 = Point(1, 2.)
    assert p1.is_equal(p2)
