from src.Geometry import Point
import pygame

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
