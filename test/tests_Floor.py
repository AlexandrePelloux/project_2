
from src.classes import *
import pytest

def floor_instantiation():
    f=Floor(4,{"coord_1":Point(3,4),"coord_2":Point(5,6)})
    assert isinstance(f,Area)
    assert f.get_floor_nb()==4

def floor_nb_int():
    with pytest.raises(Exception) as e_info:
        f=Floor(5.4,{"coord_1":Point(3,4),"coord_2":Point(5,6)})

