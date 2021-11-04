import pygame 
import numpy as np

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
        assert isinstance(point,Point)
        return(self.x <= point.x and self.y <= point.y)

    def is_equal(self,point):
        """Check if `self` and `point` are actually the same point

        Args:
            point (Point)

        Returns:
            bool
        """
        assert isinstance(point,Point)
        return (np.isclose(self.x,point.x) and np.isclose(self.y,point.y))


class BoundingBox():
    """Represent a bounding box
    """
    def __init__(self,point1,point2) -> None:
        assert (isinstance(point1,Point) and isinstance(point2,Point))
        assert (not np.isclose(point1.x,point2.x) and not np.isclose(point1.y,point2.y)),"the bounding box is flat"
        if point1.is_lower(point2):
            self.c1,self.c2=point1,point2
        else:
            self.c1,self.c2=point2,point1

    def contains(self,bounding_box) -> bool:
        """Check if self contains `bounding_box`

        Args:
            bounding_box (BoundingBox)

        Returns:
            bool
        """
        assert isinstance(bounding_box,BoundingBox)
        return (self.c1.is_lower(bounding_box.c1) and bounding_box.c2.is_lower(self.c2))

    def overlaps(self,bbox) -> bool:
        assert isinstance(bbox,BoundingBox)
        return (self.c1.x < bbox.c2.x and self.c2.x > bbox.c1.x and self.c2.y > bbox.c1.y and self.c1.y < bbox.c2.y)


    def expand(self,bounding_box) -> None:
        """Expand self to also contain `bounding_box`

        Args:
            bounding_box (BoundingBox)
        """
        assert isinstance(bounding_box,BoundingBox)
        self.c1.x=min(self.c1.x,bounding_box.c1.x)
        self.c1.y=min(self.c1.y,bounding_box.c1.y)
        self.c2.x=max(self.c2.x,bounding_box.c2.x)
        self.c2.y=max(self.c2.y,bounding_box.c2.y)

class Line():
    def __init__(self,point1,point2) -> None:
        assert (isinstance(point1,Point) and isinstance(point2,Point))
        assert (point1.x == point2.x or point1.y == point2.y), "the line is not axis-aligned"
        assert (not point1.is_equal(point2)), "the line is length 0"
        if point1.is_lower(point2):
            self.p1,self.p2=point1,point2
        else:
            self.p1,self.p2=point1,point2

    def contains(self,line)-> bool:
        assert isinstance(line,Line)
        return (self.p1.is_lower(line.p1) and line.p2.is_lower(self.p2))

    def overlaps(self,line)-> bool:
        assert isinstance(line,Line)
        return (self.contains(line) or line.contains(self) or (self.p1.is_lower(line.p1) and self.p2.is_lower(line.p2))
                or (line.p1.is_lower(self.p1) and line.p2.is_lower(self.p2)))
