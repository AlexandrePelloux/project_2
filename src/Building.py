from src.Areas import Floor
# from src.Person import Person

class Building():
    def __init__(self,floors):
        assert all(isinstance(floor,Floor) for floor in floors)
        self.contained_floors = {}
        self._people=[]
        for floor in floors:
            self.add_floor(floor)
        
    def add_floor(self,floor):
        assert isinstance(floor,Floor)
        floor_nb=floor.get_floor_nb()
        assert not floor_nb in self.contained_floors, "that floor already exists"
        self.contained_floors[floor_nb]=floor

    def add_person(self,person):
        self._people.append(person)
        #update person.containing_areas

    def remove_person(self,person):
        self._people.remove(person)
        #remove person.containing_areas
        #for each area, remove it

    def draw(self):
        pass