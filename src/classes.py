class PointCoordinates():
    """ class representing the coordinates in 2D of a point.
    """
    def __init__(self, x,y) -> None:
        """[summary] class of a point in 2D plane

        Args:
            x ([float or int]): [x coordinate]
            y ([float or int]): [y coordinate]
        """

        assert ( isinstance(x,float) or isinstance(x,int)), f"the type of 'x' coordinate is not supported, x is type {type(x)}"
        assert ( isinstance(y,float) or isinstance(y,int)), f"the type of 'y' coordinate is not supported, x is type {type(y)}"
        self.x = x
        self.y = y

    def is_lower(self,point_1):
        """Returns a bool to tell if the self point is lower (in sense of paretto) than point_1.
        Returns true if it is indeed lower else it returns false (in all other cases)

        Args:
            point_1 ([PointCoordinates]): [description]

        Raises:
            TypeError: [description]
        Returns: 
            BOOL
        """
        return(self.x <= point_1.x and self.y <= point_1.y)


class Element():
    def __init__(self,coordinates):
        """[summary]

        Args:
            coordinates ({coord_1 : PointCoordinates,coord_2 : PointCoordinates]): [coordinates of the 
            bouding box of the element.There are two points : bottom left and top right (defining a rectangle)]

        """
        assert 'coord_1' in coordinates, 'missing key coord1'
        assert 'coord_2' in coordinates, 'missing key coord2'
        assert isinstance(coordinates['coord_1'], PointCoordinates), 'wrong type for coord_1'
        assert isinstance(coordinates['coord_2'], PointCoordinates), 'wrong type for coord_2'
        self.bounding_box_coordinates = coordinates


class Area(Element):
    def __init__(self,coordinates) -> None:
        super().__init__(coordinates)
        self._assets = [] # list of element contained in Area
        self._sub_areas = [] # list of areas contained in the current Area
        self._adjacent_areas = [] # list of 'connected areas

    def addElement(self,element):
        """[summary] Add an element to the list of elements contained in the Area (assets)

        Args:
            element ([Element]): [element to add]
        """
        assert isinstance(element,Element), 'the added Element is not of type Element'
        self._assets.append(element)

class Building():
    def __init__(self,list_of_floors):
        for floor in list_of_floors:
            if not isinstance(floor,Floor):
                raise TypeError("the list of floors contains elements that aren't of type Floor")
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
