# Project 2
Second project of CS refresher


## Classes:
- *Element*:
    - Attributes:
        - Bounding box coordinates
- *Area*  :
    - Attributes
        - _assets: list of Elements
        - _subareas: list of Areas
        - _adjacent_areas
    - Methods:
        - addElement
-  *Building*:
    - Attributes:
        - Contained floors
    - Methods: 
        ad_floor:
- *PointCoordinate*:
    - Attributes:
        - x
        - y
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