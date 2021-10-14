from src.classes import *
import pytest

def test_instantiation():
    walls=[Wall({'c1':Point(1,1),'c2':Point(1,5)}),Wall({'c1':Point(1,5),'c2':Point(4,5)}),Wall({'c1':Point(4,1),'c2':Point(4,5)}),Wall({'c1':Point(1,1),'c2':Point(4,1)})]
    my_room=Room({'c1':Point(1,1),'c2':Point(4,5)},walls)
    assert isinstance(my_room,Room)

def test_wall_not_in_room():
    with pytest.raises(AssertionError):
        walls=[Wall({'c1':Point(1,1),'c2':Point(1,6)}),Wall({'c1':Point(1,5),'c2':Point(4,5)}),Wall({'c1':Point(4,1),'c2':Point(4,5)}),Wall({'c1':Point(1,1),'c2':Point(4,1)})]
        my_room=Room({'c1':Point(1,1),'c2':Point(4,5)},walls)