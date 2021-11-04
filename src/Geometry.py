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
        assert isinstance(point,Point)
        return(self.x <= point.x and self.y <= point.y)
