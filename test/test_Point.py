from src.Geometry import Point
import pytest

def test_instantiation():
    point=Point(4,5.5)
    assert isinstance(point,Point)
    assert point.x==4
    assert point.y==5.5

def test_coord_type():
    with pytest.raises(AssertionError):
        point=Point([0],1)

def test_is_lower():
    p1=Point(1,2)
    p2=Point(2,4.2)
    assert p1.is_lower(p2)

def test_is_lower_equal():
    p1=Point(1,2)
    p2=Point(1,2)
    assert p1.is_lower(p2)

def test_is_not_lower():
    p1=Point(1,2)
    p2=Point(0.9,5)
    assert not p1.is_lower(p2)
