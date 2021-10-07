from src.classes import *
import pytest

def test_instantiation():
    coord_1 = PointCoordinates(1,2)
    coord_2 = PointCoordinates(2,3)
    
    my_element = Element({'coord_1': coord_1,'coord_2': coord_2})
    assert isinstance(my_element,Element), "instantiation error"


def test_coords_are_PointCoordinates():
    with pytest.raises(AssertionError):
        my_element = Element({'coord_1':(5,4),'coord_2':PointCoordinates(1,2)})

def test_coord1_lower_coord2():
    with pytest.raises(AssertionError):
        my_element = Element({'coord_1':PointCoordinates(2,3),'coord_2':PointCoordinates(1,2)})

def test_contains():
    elem1 = Element({'coord_1':PointCoordinates(1,2),'coord_2':PointCoordinates(4,5)})
    elem2 = Element({'coord_1':PointCoordinates(2,3),'coord_2':PointCoordinates(4,5)})
    assert elem1.contains(elem2)

def test_not_contains():
    elem1 = Element({'coord_1':PointCoordinates(1,2),'coord_2':PointCoordinates(4,5)})
    elem2 = Element({'coord_1':PointCoordinates(2,3),'coord_2':PointCoordinates(3,6)})
    assert not elem1.contains(elem2)