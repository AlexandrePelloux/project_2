from src.Geometry import Point, BoundingBox
from src.Person import Person
from src.Building import Building
from src.Geometry import Point, BoundingBox
from src.Elements import Wall, Window, Door
from src.Areas import Area, Room, Floor

import pytest
import math


def test_person_instantiation():
    position = Point(1, 2)
    bounding_box = BoundingBox(Point(1, 1), Point(2, 5))
    floor = Floor(bounding_box, 0)
    bat = Building([floor])
    person = Person("personne test", bat, position, 0)
    assert isinstance(person, Person)


def test_current_floor_visited():
    """Test the list of currently visited areas is properly updated"""
    position = Point(1, 2)
    bounding_box = BoundingBox(Point(1, 1), Point(2, 5))
    floor = Floor(bounding_box, 0)
    bat = Building([floor])
    person = Person("personne test", bat, position, 0)
    assert person.current_visited_areas == [floor]


def test_floor_doesnt_exist():
    """Test we get an error if the person is located at a floor that doesn't exist"""
    position = Point(1, 2)
    bounding_box = BoundingBox(Point(1, 1), Point(2, 5))
    floor = Floor(bounding_box, 1)
    bat = Building([floor])
    with pytest.raises(AssertionError):
        person = Person("personne test", bat, position, 0)


def create_sample_building():
    """Create a building for testing purposes, containing a floor with several rooms and areas """
    wall1 = Wall(Point(1, 1), Point(1, 5))
    wall2 = Wall(Point(1, 5), Point(4, 5))
    wall3 = Wall(Point(4, 1), Point(4, 5))
    wall4 = Wall(Point(1, 1), Point(4, 1))
    room = Room([wall1, wall2, wall3, wall4])
    wall1.add_element(Window(Point(1, 2), Point(1, 3.5)))
    wall2.add_element(Door(Point(1.5, 5), Point(2, 5)))
    wall3.add_element(Door(Point(4, 2.5), Point(4, 3)))

    wall5 = Wall(Point(4, 2), Point(4, 4))
    wall6 = Wall(Point(4, 4), Point(6, 4))
    wall7 = Wall(Point(6, 4), Point(6, 2))
    wall8 = Wall(Point(6, 2), Point(4, 2))
    room2 = Room([wall5, wall6, wall7, wall8])

    wall9 = Wall(Point(6, 1), Point(8, 1))
    wall10 = Wall(Point(8, 1), Point(8, 5))
    wall11 = Wall(Point(8, 5), Point(6, 5))
    wall12 = Wall(Point(6, 5), Point(6, 1))
    room3 = Room([wall9, wall10, wall11, wall12])

    area = Area(BoundingBox(Point(1, 1), Point(4, 5)))
    area.add_subarea(room)
    area.add_subarea(room2)
    area2 = Area(BoundingBox(Point(6, 1), Point(8, 5)))
    area2.add_subarea(room3)

    floor = Floor(BoundingBox(Point(1, 1), Point(6, 6)), 4)
    floor.add_subarea(area)
    floor.add_subarea(area2)
    bat = Building([floor])
    return bat, floor, area, area2, room, room2, room3


def test_visited_areas_outside():
    """Test the visited areas are empty if the person is outside any area """
    bat, floor, area, area2, room, room2, room3 = create_sample_building()
    person = Person("personne test", bat, Point(0, 0), 4)
    assert person.current_visited_areas == []


def test_visited_areas_sample_building():
    """Test the visited areas are correct if the person is in one of the rooms """
    bat, floor, area, area2, room, room2, room3 = create_sample_building()
    person = Person("personne test", bat, Point(2, 2), 4)
    assert set(person.current_visited_areas) == set([floor, area, room])


def test_visited_areas_move():
    """Test the visited areas are updated properly as a person moves """
    bat, floor, area, area2, room, room2, room3 = create_sample_building()
    person = Person("personne test", bat, Point(2, 2), 4)
    assert set(person.current_visited_areas) == set([floor, area, room])
    person.move(Point(5, 3), 4)
    assert set(person.current_visited_areas) == set([floor, area, room2])
    person.move(Point(7, 2), 4)
    assert set(person.current_visited_areas) == set([floor, area2, room3])


def test_people_in_areas_outside():
    """Test the list of people inside the areas of the building are correct if the person is outside any area """
    bat, floor, area, area2, room, room2, room3 = create_sample_building()
    person = Person("personne test", bat, Point(0, 0), 4)
    assert all(a._people == []
               for a in [floor, area, area2, room, room2, room3])
    assert bat._people == [person]


def test_people_in_areas_sample_building():
    """Test the list of people inside the areas of the building are correct with 2 persons inside the same room """
    bat, floor, area, area2, room, room2, room3 = create_sample_building()
    person = Person("personne test", bat, Point(2, 2), 4)
    person2 = Person("personne test 2", bat, Point(2, 3), 4)
    assert all(set(a._people) == set([person, person2])
               for a in [bat, floor, area, room])
    assert all(a._people == [] for a in [area2, room2, room3])


def test_visited_areas_move():
    """Test the list of people inside the areas of the building are updated correctly as a person moves """
    bat, floor, area, area2, room, room2, room3 = create_sample_building()
    person = Person("personne test 1", bat, Point(2, 2), 4)
    assert all(a._people == [person] for a in [bat, floor, area, room])
    assert all(a._people == [] for a in [area2, room2, room3])
    person.move(Point(5, 3), 4)
    assert all(a._people == [person] for a in [bat, floor, area, room2])
    assert all(a._people == [] for a in [area2, room, room3])
    person.move(Point(7, 2), 4)
    assert set(person.current_visited_areas) == set([floor, area2, room3])
    assert all(a._people == [person] for a in [bat, floor, area2, room3])
    assert all(a._people == [] for a in [area, room, room2])
    person.exit_building()
    assert all(a._people == []
               for a in [bat, floor, area, area2, room, room2, room3])


def test_2_clusters():
    """Test that the 2 most popular locations in an area are computed correctly on a simple example """
    wall1 = Wall(Point(1, 1), Point(1, 5))
    wall2 = Wall(Point(1, 5), Point(4, 5))
    wall3 = Wall(Point(4, 1), Point(4, 5))
    wall4 = Wall(Point(1, 1), Point(4, 1))
    room = Room([wall1, wall2, wall3, wall4])
    floor = Floor(BoundingBox(Point(1, 1), Point(4, 5)), 0)
    floor.add_subarea(room)
    b = Building([floor])
    p1 = Person("p1", b, Point(1.2, 1.3), 0)
    p2 = Person("p2", b, Point(1.5, 1.0), 0)
    p3 = Person("p3", b, Point(1.4, 1.1), 0)
    p4 = Person("p4", b, Point(3.2, 3.3), 0)
    p5 = Person("p5", b, Point(2.5, 3.0), 0)
    p6 = Person("p6", b, Point(3.4, 2.9), 0)
    centers = room.calc_k_popular_places(k=2)
    assert len(centers) == 2
    assert math.floor(centers[0].x) == 3
    assert math.floor(centers[0].y) == 3
    assert math.floor(centers[1].x) == 1
    assert math.floor(centers[1].y) == 1
