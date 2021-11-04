import src.Areas as Area

class Building():
    def __init__(self,floors):
        assert all(isinstance(floor,Area.Floor) for floor in floors)
        self.contained_floors = {}
        self._people=[]
        for floor in floors:
            self.add_floor(floor)
        
    def add_floor(self,floor):
        assert isinstance(floor,Area.Floor)
        floor_nb=floor.get_floor_nb()
        assert not floor_nb in self.contained_floors, "that floor already exists"
        self.contained_floors[floor_nb]=floor

    def add_person(self,person):
        self._people.append(person)

    def remove_person(self,person):
        self._people.remove(person)

    def draw(self):
        for floor in self.contained_floors.values():
            floor.draw()