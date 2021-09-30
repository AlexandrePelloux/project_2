class Floor(Area):
    def __init__(self,floor_nb):
        """Constructor

        Args:
            floorNb (int): Floor number of the area
        """
        super().__init__()
        self.floor_nb=floor_nb

class Room(Area):
    def __init__(self):
        super().__init__()

class Corridor(Area):
    def __init__(self):
        super().__init__()

class Wall(Element):
    def __init__(self,coordinates):
        super().__init__()

class Door(Element):
    def __init__(self):
        super().__init__()

class Window(Element):
    def __init__(self):
        super().__init__()