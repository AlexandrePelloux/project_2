from src.Geometry import Point,BoundingBox
from src.Areas import Floor,Area,Room
from src.Elements import Wall,Window,Door
from src.Person import Person
import src.Building as Building


wall1=Wall(Point(1,1),Point(1,5))
wall2=Wall(Point(1,5),Point(4,5))
wall3=Wall(Point(4,1),Point(4,5))
wall4=Wall(Point(1,1),Point(4,1))
room = Room([wall1,wall2,wall3,wall4])
wall1.add_element(Window(Point(1,2),Point(1,3.5)))
wall2.add_element(Door(Point(1.5,5),Point(2,5)))
wall3.add_element(Door(Point(4,2.5),Point(4,3)))

wall5=Wall(Point(4,2),Point(4,4))
wall6=Wall(Point(4,4),Point(6,4))
wall7=Wall(Point(6,4),Point(6,2))
wall8=Wall(Point(6,2),Point(4,2))
room2 = Room([wall5,wall6,wall7,wall8])

area=Area(BoundingBox(Point(1,1),Point(4,5)))
area.add_subarea(room)
area.add_subarea(room2)
print(area.bounding_box)

test_floor = Floor(BoundingBox(Point(0,0),Point(6,6)), 4)
test_floor.add_subarea(area)
person_test = Person(Point(2,2), 'Personne_test', test_floor)
test_floor.add_person(person_test)
test_floor_2 = Floor(BoundingBox(Point(0,0),Point(6,6)), 3)
# sub_area_test = Area(bounding_box_room)
# test_floor.add_element(person_test)
# test_floor.add_subarea(sub_area_test)

test_building = Building.Building([test_floor,test_floor_2])

test_floor.draw()

#test_building.draw()