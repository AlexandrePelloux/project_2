
from src.Geometry import BoundingBox, Point
from src.Areas import Area, Floor
import pytest


def test_floor_instantiation():
    f = Floor(BoundingBox(Point(3, 4), Point(5, 6)), 4)
    assert isinstance(f, Area)
    assert isinstance(f, Floor)
    assert f.get_floor_nb() == 4


def test_floor_nb_is_int():
    with pytest.raises(AssertionError) as exception_info:
        f = Floor(BoundingBox(Point(3, 4), Point(5, 6)), 5.4)
