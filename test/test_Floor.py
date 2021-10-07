
from src.classes import *
import pytest

def test_floor_instantiation():
    f=Floor({"coord_1":PointCoordinates(3,4),"coord_2":PointCoordinates(5,6)},4)
    assert isinstance(f,Area)
    assert isinstance(f,Floor)
    assert f.get_floor_nb()==4

def test_floor_nb_is_int():
    with pytest.raises(AssertionError) as exception_info:
        f=Floor({"coord_1":PointCoordinates(3,4),"coord_2":PointCoordinates(5,6)},5.4)

