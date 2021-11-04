import pygame
import numpy as np


class Point():
    """ class representing the coordinates in 2D of a point.
    """

    def __init__(self, x, y) -> None:
        """Class of a point in 2D plane

        Args:
            x (float or int): x coordinate
            y (float or int): y coordinate
        """

        assert isinstance(
            x, (float, int)), f"the type of 'x' coordinate is not supported, x is type {type(x)}"
        assert isinstance(
            y, (float, int)), f"the type of 'y' coordinate is not supported, x is type {type(y)}"
        self.x = x
        self.y = y

    def is_lower(self, point):
        """Returns a bool to tell if the self point is lower (in sense of paretto) than point_1.
        Returns true if it is indeed lower else it returns false (in all other cases)

        Args:
            point_1 (Point)

        Returns: 
            Bool
        """
        assert isinstance(point, Point)
        return(self.x <= point.x and self.y <= point.y)

    def is_equal(self, point):
        """Check if `self` and `point` are actually the same point

        Args:
            point (Point)

        Returns:
            bool
        """
        assert isinstance(point, Point)
        return (np.isclose(self.x, point.x) and np.isclose(self.y, point.y))

    def to_pygame_coord(self, height, ratio):
        """Transform the coordinates of self by multiplying them by `ratio`
        and flipping the origin from bottom left to top left (the one used by pygame)

        Args:
            height (float): height of the pygame window
            ratio (float): scale

        Returns:
            tuple of numbers
        """
        return (self.x*ratio, height-self.y*ratio)

    def to_array(self):
        """Return the two coordinates of the Point in an array """
        return [self.x, self.y]

    def __str__(self) -> str:
        return str((self.x, self.y))

    def draw(self, height, screen, ratio, color=(255, 0, 0), thickness=3):
        coords = self.to_pygame_coord(height, ratio)
        pygame.draw.circle(screen, color, coords, thickness)


class BoundingBox():
    """Represent a rectangular, axis-aligned bounding box """

    def __init__(self, point1, point2) -> None:
        assert (isinstance(point1, Point) and isinstance(point2, Point))
        assert (not np.isclose(point1.x, point2.x) and not np.isclose(
            point1.y, point2.y)), "the bounding box is flat"
        if point1.is_lower(point2):
            self.c1, self.c2 = point1, point2
        else:
            self.c1, self.c2 = point2, point1

    def contains(self, bounding_box) -> bool:
        """Check if self contains `bounding_box`

        Args:
            bounding_box (BoundingBox)

        Returns:
            bool
        """
        assert isinstance(bounding_box, BoundingBox)
        return (self.c1.is_lower(bounding_box.c1) and bounding_box.c2.is_lower(self.c2))

    def contains_point(self, point) -> bool:
        """Check if self contains `point`

        Args:
            point (Point)

        Returns:
            bool
        """
        assert isinstance(point, Point)
        return (self.c1.is_lower(point) and point.is_lower(self.c2))

    def overlaps(self, bbox) -> bool:
        """Check if self is overlapping another bounding box

        Args:
            bbox (BoundingBox)

        Returns:
            bool
        """
        assert isinstance(bbox, BoundingBox)
        return (self.c1.x < bbox.c2.x and self.c2.x > bbox.c1.x and self.c2.y > bbox.c1.y and self.c1.y < bbox.c2.y)

    def expand(self, bounding_box) -> None:
        """Expand self to also contain `bounding_box`

        Args:
            bounding_box (BoundingBox)
        """
        assert isinstance(bounding_box, BoundingBox)
        self.c1.x = min(self.c1.x, bounding_box.c1.x)
        self.c1.y = min(self.c1.y, bounding_box.c1.y)
        self.c2.x = max(self.c2.x, bounding_box.c2.x)
        self.c2.y = max(self.c2.y, bounding_box.c2.y)

    def __str__(self) -> str:
        return "box "+str(self.c1)+" to "+str(self.c2)

    def draw(self, height, screen, ratio, color=(150, 150, 150), thickness=2):
        x1, y1 = self.c1.to_pygame_coord(height, ratio)
        x2, y2 = self.c2.to_pygame_coord(height, ratio)
        pygame.draw.rect(screen, color, [x1, y1, x2-x1, y2-y1], thickness)


class Line():
    """Represent an axis-aligned line """
    def __init__(self, point1, point2) -> None:
        assert (isinstance(point1, Point) and isinstance(point2, Point))
        assert (np.isclose(point1.x, point2.x) or np.isclose(
            point1.y, point2.y)), "the line is not axis-aligned"
        assert (not point1.is_equal(point2)), "the line is length 0"
        if point1.is_lower(point2):
            self.p1, self.p2 = point1, point2
        else:
            self.p1, self.p2 = point2, point1

    def contains(self, line) -> bool:
        """Check if `line` is included in self

        Args:
            line (Line)

        Returns:
            bool
        """
        assert isinstance(line, Line)
        return (self.p1.is_lower(line.p1) and line.p2.is_lower(self.p2))

    def overlaps(self, line) -> bool:
        """Check if self is overlapping `line`

        Args:
            line (Line)

        Returns:
            bool
        """
        assert isinstance(line, Line)
        if np.isclose(self.p1.x, line.p1.x):
            return self.p2.y > line.p1.y and self.p1.y < line.p2.y
        else:
            return self.p1.x < line.p2.x and self.p2.x > line.p1.x

    def __str__(self) -> str:
        return "line "+str(self.p1)+" to "+str(self.p2)

    def draw(self, height, screen, ratio, color=(0, 0, 0), thickness=5):
        x1, y1 = self.p1.to_pygame_coord(height, ratio)
        x2, y2 = self.p2.to_pygame_coord(height, ratio)
        pygame.draw.line(screen, color, [x1, y1], [x2, y2], thickness)
