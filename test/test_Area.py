from src.Geometry import Point,BoundingBox
from src.Areas import Area
import pytest

def test_instantiation():
    bb=BoundingBox(Point(1,2),Point(6,5))
    my_area=Area(bb)
    assert isinstance(my_area,Area)

def test_add_subarea():
    my_area=Area(BoundingBox(Point(1,2),Point(6,10)))
    second_area=Area(BoundingBox(Point(6,6),Point(8,8)))
    my_area.add_subarea(second_area)
    assert my_area.bounding_box.c1.is_equal(Point(1,2))
    assert my_area.bounding_box.c2.is_equal(Point(8,10))

def test_add_subarea_overlaps():
    my_area=Area(BoundingBox(Point(0,0),Point(10,10)))
    first_area=Area(BoundingBox(Point(1,2),Point(6,10)))
    second_area=Area(BoundingBox(Point(5,5),Point(8,8)))
    my_area.add_subarea(first_area)
    with pytest.raises(AssertionError):
        my_area.add_subarea(second_area)