from errors import FloorDontExist, NotInBuildingError
from Geometry import Point
from Building import Building
from Areas import Floor
import pygame

class Person():
    def __init__(self,position,name,floor,building=None):
        """[summary]

        Args:
            position ([Point]): [initial cordinates of the person]
            name ([str]): [name of the person]
        """
        assert isinstance(position,Point),'Position has to be of type "point_coordinates"'
        assert isinstance(floor,Floor),'floor has to be of type "Floor"'
        assert type(name)==str , 'please use a string for the name'
        assert (isinstance(building,Building) or building==None), 'building is not type Building or none'
        self.building=building
        self.current_position = position
        self.name = name
        self.current_floor = floor
    
    def move(self, delta):

        """[summary]

        Args:
            axis ([type]): [description]
            delta ([list]): [x,y,z]

        Raises:
            FloorDontExist: [description]
            NotInBuildingError: [description]
        """
        if delta[0]: #axe x
            """need to check if the deplacement is legal"""
            self.current_position.x+=delta[0]
        if delta[1]: #axe y
            """need to check if the deplacement is legal"""

            self.current_position.y+=delta[1]
        if delta[2]: #axe z
            """we have to consider the position x,y in the new floor"""
            if self.building:
                floor_to_go_to = self.current_floor._floor_nb +delta[2]
                if floor_to_go_to in self.building.contained_floors:
                    self.current_floor=self.building.contained_floors[floor_to_go_to]
                else:
                    raise FloorDontExist(f'impossible to go to floor number {floor_to_go_to}, this floor does not exist in building {self.building}')
                    
            else: 
                raise NotInBuildingError(f"Impossible to go upstairs, {self.name} is not in a building")

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
        self.current_floor.draw()