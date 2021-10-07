from src.classes import *
import pytest

def test_instantiation():
    point=PointCoordinates(4,5.5)
    assert isinstance(point,PointCoordinates)
    assert point.x==4
    assert point.y==5.5

def test_coord_type():
    with pytest.raises(AssertionError):
        point=PointCoordinates([0],1)

def test_is_lower():
    p1=PointCoordinates(1,2)
    p2=PointCoordinates(2,4.2)
    assert p1.is_lower(p2)

def test_is_lower_equal():
    p1=PointCoordinates(1,2)
    p2=PointCoordinates(1,2)
    assert p1.is_lower(p2)

def test_is_not_lower():
    p1=PointCoordinates(1,2)
    p2=PointCoordinates(0.9,5)
    assert not p1.is_lower(p2)
