from src.Geometry import Point, Line
import pytest


def test_instantiation():
    l = Line(Point(8, 3), Point(2, 3))
    assert l.p1.is_equal(Point(2, 3))
    assert l.p2.is_equal(Point(8, 3))


def test_not_axis_aligned():
    """Check we get an error if the line is not axis-aligned """
    with pytest.raises(AssertionError):
        l = Line(Point(4, 5), Point(6, 6))


def test_overlaps():
    """Test the overlaps method, when two lines are overlapping"""
    l1 = Line(Point(8, 3), Point(2, 3))
    l2 = Line(Point(1, 3), Point(2.1, 3))
    assert l1.overlaps(l2)
    assert l2.overlaps(l1)


def test_overlaps_contains():
    """Test the overlaps method, when one line contains another one"""
    l1 = Line(Point(8, 3), Point(2, 3))
    l2 = Line(Point(5, 3), Point(2.1, 3))
    assert l1.overlaps(l2)
    assert l2.overlaps(l1)


def test_not_overlaps():
    """Test the overlaps method, when two lines don't overlap """
    l1 = Line(Point(8, 3), Point(2, 3))
    l2 = Line(Point(9, 3), Point(8.1, 3))
    assert not l1.overlaps(l2)
    assert not l2.overlaps(l1)
