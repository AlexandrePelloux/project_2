# Project 2
Second project of CS refresher


## Classes:
- *Element*:
    - Attributes:
        - Bounding box coordinates
- *Area*  :
    - Attributes
        - assets: list of Elements
        - subareas: list of Areas
        - adjacentAreas
    - Methods:
        - addElement
-  *Building*:
    - Attributes:
        - Contained floors
- *Coordinate*:
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