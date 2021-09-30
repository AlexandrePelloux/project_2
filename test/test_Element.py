from src.classes import *
import pytest

def test_Element():
    coord_1 = PointCoordinates(1,2)
    coord_2 = PointCoordinates(2,3)
    
    my_element = Element({'coord_1': coord_1,'coord_2': coord_2})
    assert isinstance(my_element,Element), "erreur dans l'instanciation"