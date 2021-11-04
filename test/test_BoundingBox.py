
from src.Geometry import Point, BoundingBox
import pytest


def test_instantiation():
    bb = BoundingBox(Point(4, 5), Point(6, 6))
    assert isinstance(bb, BoundingBox)
    assert bb.c1.is_equal(Point(4, 5))
    assert bb.c2.is_equal(Point(6, 6))


def test_coord1_lower_coord2():
    bb = BoundingBox(Point(2, 3), Point(1, 2))
    assert bb.c1.is_equal(Point(1, 2))
    assert bb.c2.is_equal(Point(2, 3))


def test_flat_error():
    with pytest.raises(AssertionError):
        bb = BoundingBox(Point(2, 3), Point(2, 5))


def test_overlaps_corner():
    bb1 = BoundingBox(Point(1, 2), Point(6, 6))
    bb2 = BoundingBox(Point(5, 5), Point(7, 6))
    assert bb1.overlaps(bb2)
    assert bb2.overlaps(bb1)


def test_overlaps_contains():
    bb1 = BoundingBox(Point(1, 2), Point(6, 6))
    bb2 = BoundingBox(Point(5, 5), Point(4, 4))
    assert bb1.overlaps(bb2)
    assert bb2.overlaps(bb1)


def test_overlaps_on_side():
    bb1 = BoundingBox(Point(1, 2), Point(6, 10))
    bb2 = BoundingBox(Point(5, 6), Point(8, 8))
    assert bb1.overlaps(bb2)
    assert bb2.overlaps(bb1)


def test_not_overlaps():
    bb1 = BoundingBox(Point(1, 2), Point(6, 6))
    bb2 = BoundingBox(Point(6, 0), Point(8, 3))
    assert not bb1.overlaps(bb2)
    assert not bb2.overlaps(bb1)
