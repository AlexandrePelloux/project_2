from src.Elements import Element, Wall
from src.Geometry import BoundingBox, Point
from sklearn.cluster import KMeans
import pygame


class Area(Element):
    def __init__(self, coordinates) -> None:
        super().__init__(coordinates)
        self._assets = []  # list of element contained in Area
        self._sub_areas = []  # list of areas contained in the current Area
        self._people = []  # list of the person in current area

    def add_element(self, element):
        """Add an element to the list of elements contained in the Area (assets)

        Args:
            element (Element): element to add
        """
        assert self.contains(element)
        self._assets.append(element)

    def add_subarea(self, area):
        assert isinstance(area, Area)
        assert all(not subarea.bounding_box.overlaps(area.bounding_box)
                   for subarea in self._sub_areas), "this area overlaps with an existing subarea"
        self.expand_bounding_box(area)
        self._sub_areas.append(area)

    def draw(self, height, screen, ratio):
        for asset in self._assets:
            asset.draw(height, screen, ratio)
        for subarea in self._sub_areas:
            subarea.draw(height, screen, ratio)

    def add_person(self, person):
        if not person in self._people:
            self._people.append(person)

    def remove_person(self, person):
        if person in self._people:
            self._people.remove(person)

    def remove_person_recursively(self, person):
        if person in self._people:
            self._people.remove(person)
        for subarea in self._sub_areas:
            subarea.remove_person_recursively(person)

    def contains_person(self, person):
        return self.bounding_box.contains_point(person.current_position)

    def update_visited_areas(self, person):
        if len(self._sub_areas) > 0:
            inside_self = any(subarea.contains_person(person)
                              for subarea in self._sub_areas)
        else:
            inside_self = self.contains_person(person)
        if inside_self:
            self.add_person(person)
            person.add_visited_area(self)
        else:
            self.remove_person(person)
            person.remove_visited_area(self)
        for subarea in self._sub_areas:
            subarea.update_visited_areas(person)

    def calc_k_popular_places(self, k=2):
        persons_coords = [person.current_position.to_array()
                          for person in self._people]
        assert k < len(
            self._people), "There are not enough people to find k clusters"
        kmeans = KMeans(n_clusters=k).fit(persons_coords)
        centers = [Point(c[0], c[1]) for c in kmeans.cluster_centers_]
        return centers


class Floor(Area):
    def __init__(self, bounding_box, floor_nb):
        """Constructor

        Args:
            floorNb (int): Floor number of the area
        """
        assert isinstance(floor_nb, int)
        super().__init__(bounding_box)
        self._floor_nb = floor_nb

    def get_floor_nb(self):
        return self._floor_nb

    def draw(self):
        pygame.init()
        # define some colors
        WHITE = (255, 255, 255)
        # open a new window
        size = (700, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption(f'Floor number {self._floor_nb}')

        size_floor = (self.bounding_box.c2.x-self.bounding_box.c1.x,
                      self.bounding_box.c2.y-self.bounding_box.c1.y)
        ratio = min(size[0]/size_floor[0], size[1]/size_floor[1])
        height = size[1]

        # The loop will carry on until the user exit the game (e.g. clicks the close button).
        carryOn = True
        clock = pygame.time.Clock()
        # -------- Main Program Loop -----------
        while carryOn:
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False  # Flag that we are done so we exit this loop

            # First, clear the screen to white.
            screen.fill(WHITE)

            for element in self._assets:
                element.draw(height, screen, ratio)
            for area in self._sub_areas:
                area.draw(height, screen, ratio)
            for person in self._people:
                person.draw(height, screen, ratio)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            # --- Limit to 1  frames per second
            clock.tick(1)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()


class Room(Area):
    def __init__(self, walls):
        assert all(isinstance(wall, Wall) for wall in walls)
        assert len(walls) == 4
        c1 = walls[0].p1  # bottom left corner
        c2 = walls[0].p2  # top right corner
        for wall in walls:
            if wall.p1.is_lower(c1):
                c1 = wall.p1
            if c2.is_lower(wall.p2):
                c2 = wall.p2

        c3 = Point(c1.x, c2.y)  # top left corner
        c4 = Point(c2.x, c1.y)  # bottom right corner
        corners = [c1, c2, c3, c4]
        bounding_box = BoundingBox(c1, c2)
        # check all points defining the 4 walls are one of the 4 corners of the bounding box
        # i.e. the walls define a closed rectangle
        assert all(any(wall.p1.is_equal(c) for c in corners) for wall in walls)
        assert all(any(wall.p2.is_equal(c) for c in corners) for wall in walls)
        super().__init__(bounding_box)
        self.walls = walls

    def draw(self, height, screen, ratio):
        self.bounding_box.draw(height, screen, ratio, color=(0, 0, 0))
        for wall in self.walls:
            wall.draw(height, screen, ratio)
