from src.classes import *
import pytest

def test_instantiation():
    coord_1 = Point(1,2)
    coord_2 = Point(2,3)
    my_element = Element({'c1': coord_1,'c2': coord_2})
    assert isinstance(my_element,Element), "instantiation error"

def test_coords_are_Point():
    with pytest.raises(AssertionError):
        my_element = Element({'c1':(5,4),'c2':Point(1,2)})

def test_coord1_lower_coord2():
    with pytest.raises(AssertionError):
        my_element = Element({'c1':Point(2,3),'c2':Point(1,2)})

def test_contains():
    elem1 = Element({'c1':Point(1,2),'c2':Point(4,5)})
    elem2 = Element({'c1':Point(2,3),'c2':Point(4,5)})
    assert elem1.contains(elem2)

def test_not_contains():
    elem1 = Element({'c1':Point(1,2),'c2':Point(4,5)})
    elem2 = Element({'c1':Point(2,3),'c2':Point(3,6)})
    assert not elem1.contains(elem2)
