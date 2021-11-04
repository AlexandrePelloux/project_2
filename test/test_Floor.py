
from src.Geometry import BoundingBox, Point
from src.Areas import Area,Floor
from src.Person import Person
import pytest

def test_floor_instantiation():
    f =Floor(BoundingBox(Point(3,4),Point(5,6)),4)
    assert isinstance(f,Area)
    assert isinstance(f,Floor)
    assert f.get_floor_nb()==4

def test_floor_nb_is_int():
    with pytest.raises(AssertionError) as exception_info:
        f =Floor(BoundingBox(Point(3,4),Point(5,6)),5.4)

def test_floor_draw():
    C1 = Point(50,0) # point en haut à gauche du rectangle (décalage de C1.x vers la droite, décalage de C1.y vers le bas)
    C2 = Point(300,300) # point en bas à droite du rectangle 
    C3 = Point(75,75)
    C4 = Point(75,0)
    C5 = Point(150,150)
    bounding_box = BoundingBox(C1,C2)
    bounding_box_room = BoundingBox(C4,C5)
    test_floor  = Floor(bounding_box,4)
    person_test = Person(C3,'Personne_test',test_floor)
    sub_area_test = Area(bounding_box_room)
    test_floor.add_element(person_test)
    test_floor.add_subarea(sub_area_test)
    
    # test_floor.draw()