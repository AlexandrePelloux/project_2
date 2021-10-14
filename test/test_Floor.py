
from src.classes import *
import pytest

def test_floor_instantiation():
    f=Floor({"c1":Point(3,4),"c2":Point(5,6)},4)
    assert isinstance(f,Area)
    assert isinstance(f,Floor)
    assert f.get_floor_nb()==4

def test_floor_nb_is_int():
    with pytest.raises(AssertionError) as exception_info:
        f=Floor({"c1":Point(3,4),"c2":Point(5,6)},5.4)

