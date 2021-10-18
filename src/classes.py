from errors import *
import pygame 



class Point():
    """ class representing the coordinates in 2D of a point.
    """
    def __init__(self, x,y) -> None:
        """Class of a point in 2D plane

        Args:
            x ([float or int]): [x coordinate]
            y ([float or int]): [y coordinate]
        """

        assert isinstance(x,(float,int)), f"the type of 'x' coordinate is not supported, x is type {type(x)}"
        assert isinstance(y,(float,int)), f"the type of 'y' coordinate is not supported, x is type {type(y)}"
        self.x = x
        self.y = y

    def is_lower(self,point):
        """Returns a bool to tell if the self point is lower (in sense of paretto) than point_1.
        Returns true if it is indeed lower else it returns false (in all other cases)

        Args:
            point_1 ([Point]): [description]

        Raises:
            TypeError: [description]
        Returns: 
            BOOL
        """
        return(self.x <= point.x and self.y <= point.y)


class Element():
    def __init__(self,coordinates):
        """[summary]

        Args:
            coordinates ({coord_1 : Point,coord_2 : Point]): [coordinates of the 
            bouding box of the element.There are two points : bottom left and top right (defining a rectangle)]

        """
        assert 'c1' in coordinates, 'missing key coord1'
        assert 'c2' in coordinates, 'missing key coord2'
        assert isinstance(coordinates['c1'], Point), 'wrong type for coord_1'
        assert isinstance(coordinates['c2'], Point), 'wrong type for coord_2'
        assert coordinates['c1'].is_lower(coordinates['c2']), 'coord_1 is not lower than coord_2'
        self.bounding_box = coordinates
    
    def contains(self,elem):
        """Check if self's bounding box contains elem

        Args:
            elem (Element)

        Returns:
            Bool
        """
        assert isinstance(elem,Element)
        return (self.bounding_box['c1'].is_lower(elem.bounding_box['c1']) and elem.bounding_box['c2'].is_lower(self.bounding_box['c2']))

    def expand_bounding_box(self,element):
        assert isinstance(element,Element)
        self.bounding_box['c1'].x=min(self.bounding_box['c1'].x,element.bounding_box['c1'].x)
        self.bounding_box['c1'].y=min(self.bounding_box['c1'].y,element.bounding_box['c1'].y)
        self.bounding_box['c2'].x=max(self.bounding_box['c2'].x,element.bounding_box['c2'].x)
        self.bounding_box['c2'].y=max(self.bounding_box['c2'].y,element.bounding_box['c2'].y)
    
    def draw(self,screen,is_area=False):
        COLOR = {(0,156,65),(45,178,200),(158,20,46)}
        my_color= COLOR.pop() # choose one color among a set of colors
        if is_area:
            print('Call to Element.draw() with is_area=True')
            print('coordinates of C4: ',self.bounding_box['c1'].x,self.bounding_box['c1'].y)
            pygame.draw.rect(screen, my_color, [self.bounding_box['c1'].x,self.bounding_box['c1'].y,self.bounding_box['c2'].x,self.bounding_box['c2'].y],5) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]

        else:
            pygame.draw.rect(screen, my_color, [self.bounding_box['c1'].x,self.bounding_box['c1'].y,self.bounding_box['c2'].x,self.bounding_box['c2'].y]) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]


class Area(Element):
    def __init__(self,coordinates) -> None:
        super().__init__(coordinates)
        self._assets = [] # list of element contained in Area
        self._sub_areas = [] # list of areas contained in the current Area
        # self._adjacent_areas = [] # list of 'connected areas

    def add_element(self,element):
        """Add an element to the list of elements contained in the Area (assets)

        Args:
            element (Element): element to add
        """
        #assert self.contains(element) TODO : add a person
        self._assets.append(element)

    def add_subarea(self,area):
        assert isinstance(area,Area)
        self.expand_bounding_box(area)
        self._sub_areas.append(area)
    
    def draw(self,screen):
        print('call to area.draw()')
        print('coordinates of C4 before: ',self.bounding_box['c1'].x,self.bounding_box['c1'].y)

        super().draw(screen,is_area=True)



class Building():
    def __init__(self,floors):
        assert all(isinstance(floor,Floor) for floor in floors)
        self.contained_floors = floors  # list of the floors in the building 



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

    def draw(self):
        # initialize game ingine:
        pygame.init()
        # define some colors 
        BLACK = (0,0,0)
        WHITE = ( 255, 255, 255)
        GREEN = ( 0, 255, 0)
        RED = ( 255, 0, 0)
        # open a new window 
        size = (700,500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption(f'This is the representation of the floor number {self._floor_nb}')
        # The loop will carry on until the user exit the game (e.g. clicks the close button).
        carryOn = True
        
        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()
        
        
        # -------- Main Program Loop -----------
        while carryOn:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    carryOn = False # Flag that we are done so we exit this loop
        
            # --- Game logic should go here
        
            # --- Drawing code should go here
            # First, clear the screen to white. 
            screen.fill(WHITE)
            #The you can draw different shapes and lines or add text to your background stage.

            # TODO : creer des méthodes draw qui prennent screen en paramètre pour dessiner des trucs dans chacuns des sous objets sur le même écran
            
            for element in self._assets:
                element.draw(screen)
            print(self._sub_areas)    
            for area in self._sub_areas:
                area.draw(screen)

            # TODO : Draw the person in the floor

            # draw the area corresponding to the floor. 
            pygame.draw.rect(screen, RED, [self.bounding_box['c1'].x,self.bounding_box['c1'].y,self.bounding_box['c2'].x,self.bounding_box['c2'].y],5) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]
            
            #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
            #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
        
        
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
            # --- Limit to 1  frames per second
            
            clock.tick(1)
        
        #Once we have exited the main program loop we can stop the game engine:
        pygame.quit()

class Room(Area):
    def __init__(self,bounding_box,walls):
        assert all(isinstance(wall,Wall) for wall in walls)
        assert len(walls)==4
        super().__init__(bounding_box)
        assert all(self.contains(wall) for wall in walls)

# class Corridor(Area):
#     def __init__(self,bounding_box):
#         super().__init__(bounding_box)


class Wall(Element):
    def __init__(self,coords):
        super().__init__(coords)
        assert (coords['c1'].x==coords['c2'].x or coords['c1'].y==coords['c2'].y), "not along an axis"
        self._subelements=[]

    def add_element(self,element):
        assert self.contains(element)
        self._subelements.append(element)

class Door(Element):
    def __init__(self,coords):
        assert (coords['c1'].x==coords['c2'].x or coords['c1'].y==coords['c2'].y), "not along an axis"
        super().__init__(coords)

    def draw(self):
        pass
class Window(Element):
    def __init__(self,coords):
        assert (coords['c1'].x==coords['c2'].x or coords['c1'].y==coords['c2'].y), "not along an axis"
        super().__init__(coords)


"""/!\ TODO : Méthodes d'affichage des éléments"""

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
                list_of_floors = [floor for floor in self.building.contained_floors]
                list_of_floor_nb = []
                for floor in list_of_floors:
                    list_of_floor_nb.append(floor._floor_nb)
                if floor_to_go_to in list_of_floor_nb:
                    index = list_of_floor_nb.index(floor_to_go_to)
                    self.current_floor=list_of_floors[index]
                else:
                    raise FloorDontExist(f'impossible to go to floor number {floor_to_go_to}, this floor does not exist in building {self.building}')
                    
            else: 
                raise NotInBuildingError(f"Impossible to go upstairs, {self.name} is not in a building")

    def draw(self,screen):
        print('Calling person.draw()...')
        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 20) # check size of the police
        textsurface = myfont.render(self.name, False, (0, 0, 0)) 
        screen.blit(textsurface,(self.current_position.x,self.current_position.y))# display the name of the person
        my_color = (250,0,0)
        pygame.draw.circle(screen, my_color, (self.current_position.x,self.current_position.y),5) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]


if __name__=='__main__':
    C1 = Point(50,0) # point en haut à gauche du rectangle (décalage de C1.x vers la droite, décalage de C1.y vers le bas)
    C2 = Point(300,300) # point en bas à droite du rectangle 
    C3 = Point(75,75)
    C4 = Point(75,0)
    C5 = Point(150,150)
    bounding_box = {'c1':C1,'c2': C2}
    bounding_box_room = {'c1':C4,'c2':C5}
    test_floor  = Floor(bounding_box,4)
    person_test = Person(C3,'Personne_test',test_floor)
    sub_area_test = Area(bounding_box_room)
    test_floor.add_element(person_test)
    test_floor.add_subarea(sub_area_test)
    
    test_floor.draw()