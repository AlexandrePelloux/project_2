from src.classes import *
import pytest

def test_person_instaciation():
    position = PointCoordinates(1,2)
    coordinates = { 'coord_1' : PointCoordinates(1,1), 'coord_2' : PointCoordinates(2,5)}
    floor = Floor(coordinates,0)
    bat= Building([floor])
    person = Person(position,'personne test',floor,bat)
    assert isinstance(person,Person)

def test_move_person_x_axis():
    position = PointCoordinates(1,2)
    coordinates = { 'coord_1' : PointCoordinates(1,1), 'coord_2' : PointCoordinates(2,5)}
    floor = Floor(coordinates,0)
    bat= Building([floor])
    person = Person(position,'personne test',floor,bat)
    person.move([1,0,0])
    assert person.current_position.x==2

def test_move_person_y_axis():
    position = PointCoordinates(1,2)
    coordinates = { 'coord_1' : PointCoordinates(1,1), 'coord_2' : PointCoordinates(2,5)}
    floor = Floor(coordinates,0)
    bat= Building([floor])
    person = Person(position,'personne test',floor,bat)
    person.move([0,1,0])
    assert person.current_position.y==3

def test_move_person_z_axis():
    position = PointCoordinates(1,2)
    coordinates = { 'coord_1' : PointCoordinates(1,1), 'coord_2' : PointCoordinates(2,5)}
    floor0 = Floor(coordinates,0)
    floor1 = Floor(coordinates,1)
    bat= Building([floor0,floor1])
    person = Person(position,'personne test',floor0,bat)
    person.move([0,0,1])
    assert person.current_floor._floor_nb == 1

def test_move_person_z_axis_floor_dosent_exist():
    with pytest.raises(FloorDontExist):
        position = PointCoordinates(1,2)
        coordinates = { 'coord_1' : PointCoordinates(1,1), 'coord_2' : PointCoordinates(2,5)}
        floor0 = Floor(coordinates,0)
        floor1 = Floor(coordinates,1)
        bat= Building([floor0,floor1])
        person = Person(position,'personne test',floor0,bat)
        person.move([0,0,2])

def test_move_person_z_axis_building_doesnt_exist():
    with pytest.raises(NotInBuildingError):
        position = PointCoordinates(1,2)
        coordinates = { 'coord_1' : PointCoordinates(1,1), 'coord_2' : PointCoordinates(2,5)}
        floor0 = Floor(coordinates,0)
        floor1 = Floor(coordinates,1)
        bat= Building([floor0,floor1])
        person = Person(position,'personne test',floor0)
        person.move([0,0,2])