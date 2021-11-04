from src.Geometry import Point,BoundingBox
from src.Elements import Wall,Window,Door
from src.Areas import Area,Room,Floor
from src.Person import Person


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

wall9=Wall(Point(6,1),Point(8,1))
wall10=Wall(Point(8,1),Point(8,5))
wall11=Wall(Point(8,5),Point(6,5))
wall12=Wall(Point(6,5),Point(6,1))
room3 = Room([wall9,wall10,wall11,wall12])

area=Area(BoundingBox(Point(1,1),Point(4,5)))
area.add_subarea(room)
area.add_subarea(room2)
area2=Area(BoundingBox(Point(6,1),Point(8,5)))
area2.add_subarea(room3)

test_floor = Floor(BoundingBox(Point(0,0),Point(6,6)), 4)
test_floor.add_subarea(area)
test_floor.add_subarea(area2)
# person_test = Person(C3, 'Personne_test', test_floor)
# sub_area_test = Area(bounding_box_room)
# test_floor.add_element(person_test)
# test_floor.add_subarea(sub_area_test)
test_floor.draw()