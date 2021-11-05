from src.Geometry import Point
from src.Elements import Wall, Door, Window
import pytest


def test_instantiation():
    w = Wall(Point(8, 3), Point(2, 3))
    assert w.p1.is_equal(Point(2, 3))
    assert w.p2.is_equal(Point(8, 3))


def test_not_axis_aligned():
    """Check we get an error if the wall is not axis-aligned """
    with pytest.raises(AssertionError):
        w = Wall(Point(4, 5), Point(6, 6))


def test_add_window():
    """Check we can add a window to a wall """
    w = Wall(Point(8, 3), Point(2, 3))
    window = Window(Point(2.5, 3), Point(3.5, 3))
    w.add_element(window)
    w._subelements[0] == window


def test_add_door():
    """Check we can add a door to a wall """
    w = Wall(Point(8, 3), Point(2, 3))
    door = Door(Point(2.5, 3), Point(3.5, 3))
    w.add_element(door)
    w._subelements[0] == door


def test_add_overlapping_elements():
    """Check a wall cannot contain two overlapping elements (window/door...) """
    w = Wall(Point(8, 3), Point(2, 3))
    window = Window(Point(2.5, 3), Point(3.5, 3))
    door = Door(Point(3, 3), Point(4, 3))
    w.add_element(window)
    with pytest.raises(AssertionError):
        w.add_element(door)
