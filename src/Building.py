from src.Areas import Floor

class Building():
    def __init__(self,floors):
        assert all(isinstance(floor,Floor) for floor in floors)
        self.contained_floors = floors  # list of the floors in the building 
        

