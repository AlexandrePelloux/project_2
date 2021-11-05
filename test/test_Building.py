
from src.Building import Building
from src.Geometry import Point, BoundingBox
from src.Areas import Floor
from src.Person import Person

import pytest


def test_instantiation():
    floor1 = Floor(BoundingBox(Point(1, 1), Point(5, 5)), 0)
    floor2 = Floor(BoundingBox(Point(1, 1), Point(5, 5)), 2)
    bat = Building([floor1, floor2])
    assert isinstance(bat, Building)
    assert bat.contained_floors[0] == floor1
    assert bat.contained_floors[2] == floor2


def test_add_floors():
    floor1 = Floor(BoundingBox(Point(1, 1), Point(5, 5)), 0)
    floor2 = Floor(BoundingBox(Point(1, 1), Point(5, 5)), 2)
    bat = Building()
    bat.add_floor(floor1)
    bat.add_floor(floor2)
    assert bat.contained_floors[0] == floor1
    assert bat.contained_floors[2] == floor2


def test_multiple_same_floor():
    floor1 = Floor(BoundingBox(Point(1, 1), Point(5, 5)), 1)
    floor2 = Floor(BoundingBox(Point(1, 1), Point(5, 5)), 1)
    bat = Building()
    bat.add_floor(floor1)
    with pytest.raises(AssertionError):
        bat.add_floor(floor2)

def test_add_person():
    person = Person("personne test")
    bat = Building()
    bat.add_person(person)
    assert bat._people==[person]

def test_add_person_twice():
    person = Person("personne test")
    bat = Building()
    bat.add_person(person)
    bat.add_person(person)
    assert bat._people==[person]

def test_remove_person():
    person = Person("personne test")
    bat = Building()
    bat.add_person(person)
    bat.remove_person(person)
    assert bat._people==[]


def test_remove_absent_person():
    person = Person("personne test")
    bat = Building()
    bat.remove_person(person)
    assert bat._people==[]