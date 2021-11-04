from src.Geometry import BoundingBox, Line
import pygame


class Element():
    def __init__(self, bounding_box):
        """Abstract Element class

        Args:
            bounding_box (BoundingBox): "rectangle" representing an element
        """
        assert isinstance(bounding_box, BoundingBox)
        self.bounding_box = bounding_box

    def contains(self, elem):
        """Check if self's bounding box contains elem

        Args:
            elem (Element)

        Returns:
            Bool
        """
        assert isinstance(elem, Element)
        return self.bounding_box.contains(elem.bounding_box)

    def expand_bounding_box(self, element):
        """Expand the bounding box of self to also contain the bounding box of `element`

        Args:
            element (Element)
        """
        assert isinstance(element, Element)
        self.bounding_box.expand(element.bounding_box)

    def draw(self, height, screen, ratio):
        self.bounding_box.draw(height, screen, ratio)


class Wall(Line):
    def __init__(self, p1, p2):
        """Represent a wall, which can contain other elements like doors and windows"""
        super().__init__(p1, p2)
        self._subelements = []

    def add_element(self, element):
        """Add an element to the wall """
        assert self.contains(element), "this element is not in the wall"
        assert all(not el.overlaps(element)
                   for el in self._subelements), "this new element is overlapping an existing subelement"
        self._subelements.append(element)

    def draw(self, height, screen, ratio):
        for element in self._subelements:
            element.draw(height, screen, ratio)


class Door(Line):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)

    def draw(self, height, screen, ratio):
        super().draw(height, screen, ratio, (0, 250, 0))


class Window(Line):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)

    def draw(self, height, screen, ratio):
        super().draw(height, screen, ratio, (0, 0, 250))
