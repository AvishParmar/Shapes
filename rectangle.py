# Avish Parmar 112647892
from quadrilateral import Quadrilateral
from two_d_point import TwoDPoint


class Rectangle(Quadrilateral):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A rectangle cannot be formed by the given coordinates.")

    def __is_member(self):  # Check if x and y are same for vertices
        """Returns True if the given coordinates form a valid rectangle, and False otherwise."""
        return self.vertices[1].y == self.vertices[0].y and self.vertices[1].x == self.vertices[2].x and \
            self.vertices[2].y == self.vertices[3].y and self.vertices[0].x == self.vertices[3].x

    def center(self):
        """Returns the center of this rectangle, calculated to be the point of intersection of its diagonals."""
        # center of rectangle = ((x1+x2)/2, (y1+y2)/2)
        first_point = self.vertices[0]
        second_point = self.vertices[2]

        center_point_x, center_point_y = (first_point.x + second_point.x) / 2, (first_point.y + second_point.y) / 2
        return TwoDPoint(center_point_x, center_point_y)

    def area(self):  # Length * width
        """Returns the area of this rectangle. The implementation invokes the side_lengths() method from the superclass,
                and computes the product of this rectangle's length and width."""
        side_lengths = self.side_lengths()
        area = side_lengths[0] * side_lengths[1]
        return round(area, 5)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.vertices[0].x == other.vertices[0].x and self.vertices[0].y == other.vertices[0].y and \
                   self.vertices[1].x == other.vertices[1].x and self.vertices[1].y == other.vertices[1].y and \
                   self.vertices[2].x == other.vertices[2].x and self.vertices[2].y == other.vertices[2].y and \
                   self.vertices[3].x == other.vertices[3].x and self.vertices[3].y == other.vertices[3].y and \
                   self.area() == other.area() and self.center() == other.center() and \
                   self.side_lengths() == other.side_lengths()
        else:
            return False

    def __str__(self):
        return "Rectangle:\nVertex 0: (" + str(self.vertices[0].x) + ", " + str(self.vertices[0].y) + ")\n" + \
               "Vertex 1: (" + str(self.vertices[1].x) + ", " + str(self.vertices[1].y) + ")\n" + \
               "Vertex 2: (" + str(self.vertices[2].x) + ", " + str(self.vertices[2].y) + ")\n" + \
               "Vertex 3: (" + str(self.vertices[3].x) + ", " + str(self.vertices[3].y) + ")\n" + \
               "Area: " + str(self.area()) + "\n" + "Center: (" + str(self.center().x) + ", " + str(
            self.center().y) + ")"
