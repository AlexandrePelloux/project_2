from src.classes import *
from pytest import *

def test_Element():
    coord_1 = PointCoordinates(1,2)
    coord_2 = PointCoordinates(2,3)
    my_element = Element({'coord_1': coord_1,'coord_2': coord_2})
    assert isinstance(my_element,Element), "erreur dans l'instanciation"

def test_if0():
    if 0:
        assert(0==1),'on est entré dans le if 0'