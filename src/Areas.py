from Elements import Element,Wall
from Geometry import BoundingBox, Point
import pygame

class Area(Element):
    def __init__(self,coordinates) -> None:
        super().__init__(coordinates)
        self._assets = [] # list of element contained in Area
        self._sub_areas = [] # list of areas contained in the current Area

    def add_element(self,element):
        """Add an element to the list of elements contained in the Area (assets)

        Args:
            element (Element): element to add
        """
        assert self.contains(element) #TODO : add a person
        self._assets.append(element)

    def add_subarea(self,area):
        assert isinstance(area,Area)
        assert all(not subarea.bounding_box.overlaps(area.bounding_box) for subarea in self._sub_areas), "this area overlaps with an existing subarea"
        self.expand_bounding_box(area)
        self._sub_areas.append(area)
    # TODO modify this
    def draw(self,screen):
        print('call to area.draw()')
        print('coordinates of C4 before: ',self.bounding_box.c1.x,self.bounding_box.c1.y)

        super().draw(screen,is_area=True)



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
            pygame.draw.rect(screen, RED, [self.bounding_box.c1.x,self.bounding_box.c1.y,self.bounding_box.c2.x,self.bounding_box.c2.y],5) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]
            
            #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
            #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
        
        
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
            # --- Limit to 1  frames per second
            
            clock.tick(1)
        
        #Once we have exited the main program loop we can stop the game engine:
        pygame.quit()

class Room(Area):
    def __init__(self,walls):
        assert all(isinstance(wall,Wall) for wall in walls)
        assert len(walls)==4
        c1=walls[0].p1  #bottom left corner
        c2=walls[0].p2  #top right corner
        for wall in walls:
            if wall.p1.is_lower(c1):
                c1=wall.p1
            if c2.is_lower(wall.p2):
                c2=wall.p2
        
        c3=Point(c1.x,c2.y) #top left corner
        c4=Point(c2.x,c1.y) #bottom right corner
        corners=[c1,c2,c3,c4]
        bounding_box=BoundingBox(c1,c2)
        #check all points defining the 4 walls are one of the 4 corners of the bounding box
        #i.e. the walls define a closed rectangle
        assert all(any(wall.p1.is_equal(c) for c in corners) for wall in walls)
        assert all(any(wall.p2.is_equal(c) for c in corners) for wall in walls)
        super().__init__(bounding_box)
        self.walls=walls
    
    # TODO completer ca
    def draw(self,screen):
        pass
