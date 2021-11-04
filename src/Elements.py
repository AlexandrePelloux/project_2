from Geometry import BoundingBox, Point, Line
import pygame

class Element():
    def __init__(self,bounding_box):
        """[summary]

        Args:
            bouding box of the element. There are two points : bottom left and top right (defining a rectangle)

        """
        assert isinstance(bounding_box,BoundingBox)
        self.bounding_box = bounding_box

    def contains(self,elem):
        """Check if self's bounding box contains elem

        Args:
            elem (Element)

        Returns:
            Bool
        """
        assert isinstance(elem,Element)
        return self.bounding_box.contains(elem.bounding_box)

    def expand_bounding_box(self,element):
        assert isinstance(element,Element)
        self.bounding_box.expand(element.bounding_box)
        
    # TODO : check if this is correct
    def draw(self,screen,is_area=False):
        COLOR = {(0,156,65),(45,178,200),(158,20,46)}
        my_color= COLOR.pop() # choose one color among a set of colors
        if is_area:
            print('Call to Element.draw() with is_area=True')
            print('coordinates of C4: ',self.bounding_box.c1.x,self.bounding_box.c1.y)
            pygame.draw.rect(screen, my_color, [self.bounding_box.c1.x,self.bounding_box.c1.y,self.bounding_box.c2.x,self.bounding_box.c2.y],5) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]

        else:
            pygame.draw.rect(screen, my_color, [self.bounding_box.c1.x,self.bounding_box.c1.y,self.bounding_box.c2.x,self.bounding_box.c2.y]) # rectangle coordinates are represented by [c1.x,c1.y,c2.x,c2.y]


class Wall(Line):
    def __init__(self,p1,p2):
        super().__init__(p1,p2)
        self._subelements=[]

    def add_element(self,element):
        assert self.contains(element)
        assert all(not el.overlaps(element) for el in self._subelements), "this new element is overlapping an existing subelement"
        self._subelements.append(element)

class Door(Line):
    def __init__(self,p1,p2):
        super().__init__(p1,p2)

    def draw(self):
        pass
class Window(Line):
    def __init__(self,p1,p2):
        super().__init__(p1,p2)

    def draw(self):
        pass
