class PointCoordinates():
    """ class representing the coordinates in 2D of a point.
    """
    def __init__(self, coord_dict) -> None:
        """[(constructor of PointCoordinates class)]

        Args:
            coord_dict ([dictionary]): [looks like : { 'x' : value of coordinate x, 'y' : value of y coordinate}]
        """
        self.x = coord_dict['x']
        self.y = coord_dict['y']

class Element():
    def __init__(self,coordinates):
        """[summary]

        Args:
            coordinates ({coord_1 : PointCoordinates,coord_2 : PointCoordinates]): [coordinates of the 
            bouding box of the element.There are two points : bottom left and top right (defining a rectangle)]

        """
        self.bounding_box_coordinates = coordinates


class Area():
    def __init__(self) -> None:
        self._assets = [] # list of element contained in Area
        self._sub_areas = [] # list of areas contained in the current Area
        self._adjacent_areas = [] # list of 'connected areas

    def addElement(self,element):
        """[summary] Add an element to the list of elements contained in the Area (assets)

        Args:
            element ([Element]): [element to add]
        """
        self._assets.append(element)

class Building():
    def __init__(self,list_of_floors):
        self.contained_floors = list_of_floors # list of the floors in the building 



class Floor(Area):
    def __init__(self,bounding_box,floor_nb):
        """Constructor

        Args:
            floorNb (int): Floor number of the area
        """
        assert isinstance(floor_nb,int)
        super().__init__(bounding_box)
        self._floor_nb=floor_nb
    
    def get_floor_nb(self):
        return self._floor_nb

class Room(Area):
    def __init__(self,bounding_box):
        super().__init__(bounding_box)

class Corridor(Area):
    def __init__(self,bounding_box):
        super().__init__(bounding_box)

class Wall(Element):
    def __init__(self,bounding_box):
        super().__init__(bounding_box)

class Door(Element):
    def __init__(self,bounding_box):
        super().__init__(bounding_box)

class Window(Element):
    def __init__(self,bounding_box):
        super().__init__(bounding_box)
