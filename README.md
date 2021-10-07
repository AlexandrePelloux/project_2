# Project 2
Second project of CS refresher


## Classes:
- *Element*:
    - Attributes:
        - Bounding box coordinates : {p1:PointCoordinates,p2:PointCoordinates} where p1 < p2
    - Methodes:
        - contains(Element): Element's bounding box is inside self's
- *Area* inheriting from *Element* :
    - Attributes
        - _assets: list of Elements
        - _subareas: list of Areas
    - Methods:
        - add_element (check if element is inside self's bounding box)
        - add_subarea (need to expand the bounding box coordinates accordingly)
-  *Building*:
    - Attributes:
        - Contained floors
    - Methods: 
        add_floor:
- *PointCoordinate*:
    - Attributes:
        - x
        - y
    - Methodes:
        - is_lower
---
## Inheriting from *Area*
- *Floor* 
    - Attributes:
        - floorNb: Int
- *Room*
- *Corridor* 

---
## Inheriting from *Element*
-  *Wall*  :
    - Attributes:
        - containedElements
-  *Door* 
    - Attributes:
        - linkedAreas: tuple of Areas
-  *Window* 
-  *Stairs* :
    - Attributes:
        - floorUp:
        - floorDown