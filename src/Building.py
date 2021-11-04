from src.Areas import Floor

class Building():
    def __init__(self,floors):
        assert all(isinstance(floor,Floor) for floor in floors)
        self.contained_floors = {}
        for floor in floors:
            self.add_floor(floor)
        
    def add_floor(self,floor):
        assert isinstance(floor,Floor)
        floor_nb=floor.get_floor_nb()
        assert not floor_nb in self.contained_floors, "that floor already exists"
        self.contained_floors[floor_nb]=floor

    def draw(self):
        pass