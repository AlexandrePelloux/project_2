from src.Geometry import Point,BoundingBox
from src.Areas import Room
from src.Elements import Wall
import pytest

def test_instantiation():
    wall1=Wall(Point(1,1),Point(1,5))
    wall2=Wall(Point(1,5),Point(4,5))
    wall3=Wall(Point(4,1),Point(4,5))
    wall4=Wall(Point(1,1),Point(4,1))
    walls=[wall1,wall2,wall3,wall4]
    my_room=Room(walls)
    assert isinstance(my_room,Room)
    assert my_room.bounding_box.c1.is_equal(Point(1,1))
    assert my_room.bounding_box.c2.is_equal(Point(4,5))

def test_walls_not_rectangle():
    with pytest.raises(AssertionError):
        wall1=Wall(Point(1,1),Point(1,6))
        wall2=Wall(Point(1,5),Point(4,5))
        wall3=Wall(Point(4,1),Point(4,5))
        wall4=Wall(Point(1,1),Point(4,1))
        walls=[wall1,wall2,wall3,wall4]
        my_room=Room(walls)

def test_walls_not_closed():
    with pytest.raises(AssertionError):
        wall1=Wall(Point(1,1),Point(1,4))
        wall2=Wall(Point(1,5),Point(4,5))
        wall3=Wall(Point(4,1),Point(4,5))
        wall4=Wall(Point(1,1),Point(4,1))
        walls=[wall1,wall2,wall3,wall4]
        my_room=Room(walls)