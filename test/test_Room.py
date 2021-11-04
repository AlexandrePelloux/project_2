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
    my_room=Room(BoundingBox(Point(1,1),Point(4,5)),walls)
    assert isinstance(my_room,Room)

# def test_wall_not_in_room():
#     with pytest.raises(AssertionError):
#         walls=[Wall({'c1':Point(1,1),'c2':Point(1,6)}),Wall({'c1':Point(1,5),'c2':Point(4,5)}),Wall({'c1':Point(4,1),'c2':Point(4,5)}),Wall({'c1':Point(1,1),'c2':Point(4,1)})]
#         my_room=Room({'c1':Point(1,1),'c2':Point(4,5)},walls)