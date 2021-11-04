
from src.Geometry import Point,BoundingBox
import pytest

def test_instantiation():
    bb=BoundingBox(Point(4,5),Point(6,6))
    assert isinstance(bb,BoundingBox)
    assert bb.c1.is_equal(Point(4,5))
    assert bb.c2.is_equal(Point(6,6))

def test_coord1_lower_coord2():
    bb = BoundingBox(Point(2,3),Point(1,2))
    assert bb.c1.is_equal(Point(1,2))
    assert bb.c2.is_equal(Point(2,3))

def test_flat_error():
    with pytest.raises(AssertionError):
        bb=BoundingBox(Point(2,3),Point(2,5))