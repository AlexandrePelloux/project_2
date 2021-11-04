from src.Geometry import BoundingBox, Point
from src.Elements import Element
import pytest

def test_instantiation():
    coord_1 = Point(1,2)
    coord_2 = Point(2,3)
    my_element = Element(BoundingBox(coord_1,coord_2))
    assert isinstance(my_element,Element), "instantiation error"

def test_coords_are_Point():
    with pytest.raises(AssertionError):
        my_element = Element(BoundingBox((5,4),Point(1,2)))

def test_contains():
    elem1 = Element(BoundingBox(Point(1,2),Point(4,5)))
    elem2 = Element(BoundingBox(Point(2,3),Point(4,5)))
    assert elem1.contains(elem2)

def test_not_contains():
    elem1 = Element(BoundingBox(Point(1,2),Point(4,5)))
    elem2 = Element(BoundingBox(Point(2,3),Point(3,6)))
    assert not elem1.contains(elem2)
