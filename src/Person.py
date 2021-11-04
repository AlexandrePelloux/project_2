from src.errors import FloorDontExist, NotInBuildingError
from src.Geometry import Point
from src.Building import Building
from src.Areas import Area
import pygame

class Person():
    def __init__(self,name,building=None,position=None,floor=None):
        """[summary]

        Args:
            position ([Point]): [initial cordinates of the person]
            name ([str]): [name of the person]
        """
        assert isinstance(name,str),'please use a string for the name'
        assert (isinstance(position,Point) or position is None),'Position has to be of type "point_coordinates" or None'
        assert (isinstance(floor,int) or floor is None),'floor has to be of type "Int" or None'
        assert (isinstance(building,Building) or building is None), 'building is not type Building or none'

        self.name = name
        self.current_visited_areas=[]
        self.building=None
        self.current_floor=None
        self.current_position=None

        if not building is None:
            self.enter_building(building)
            if not floor is None and not position is None:
                self.move(position,floor)
    
    def enter_building(self,building):
        assert isinstance(building,Building)
        assert self.building is None, "This person is already in a building"
        self.building=building
        self.building.add_person(self)

    def exit_building(self):
        assert not self.building is None, "This person is not in a building"
        self.building.remove_person(self)
        self.current_floor.remove_person_recursively(self)
        self.building=None
        self.current_floor=None

    def add_visited_area(self,area):
        assert isinstance(area,Area)
        print("person:add visited area")
        print(area.bounding_box)
        if not area in self.current_visited_areas:
            self.current_visited_areas.append(area)

    def remove_visited_area(self,area):
        assert isinstance(area,Area)
        if area in self.current_visited_areas:
            self.current_visited_areas.remove(area)
    
    def move(self,new_position,floor_number):

        """[summary]

        Args:
            axis ([type]): [description]

        Raises:
            FloorDontExist: [description]
            NotInBuildingError: [description]
        """
        assert isinstance(new_position,Point)
        assert floor_number in self.building.contained_floors, "this floor does not exist in the current building"
        self.current_position=new_position
        if self.current_floor is None or self.current_floor.get_floor_nb()!=floor_number:
            if not self.current_floor is None:
                self.current_floor.remove_person_recursively(self)
            self.current_floor=self.building.contained_floors[floor_number]
        self.current_floor.update_visited_areas(self)



    # def draw(self,screen):
    #     print('Calling person.draw()...')
    #     pygame.font.init() # you have to call this at the start, 
    #                # if you want to use this module.
    #     myfont = pygame.font.SysFont('Comic Sans MS', 20) # check size of the police
    #     textsurface = myfont.render(self.name, False, (0, 0, 0)) 
    #     screen.blit(textsurface,(self.current_position.x,self.current_position.y))# display the name of the person
    #     my_color = (250,0,0)
    #     pygame.draw.circle(screen, my_color, (self.current_position.x,self.current_position.y),5) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]

    def draw(self,screen):
        self.current_position.draw()