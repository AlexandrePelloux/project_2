from src.classes import *
import pytest

def test_instantiation():
    my_area=Area({'c1':Point(1,2),'c2':Point(6,5)})
    assert isinstance(my_area,Area)

def test_expand_bounding_box():
    my_area=Area({'c1':Point(1,2),'c2':Point(6,10)})
    second_area=Area({'c1':Point(6,6),'c2':Point(8,8)})
    my_area.add_subarea(second_area)
    assert my_area.bounding_box['c1'].x==1
    assert my_area.bounding_box['c1'].y==2
    assert my_area.bounding_box['c2'].x==8
    assert my_area.bounding_box['c2'].y==10