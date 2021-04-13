# Avish Parmar 112647892
from typing import List


class TwoDPoint:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TwoDPoint):
            return self.x == other.x and self.y == other.y
        else:
            return False  # TODO

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return '(%g, %g)' % (self.__x, self.__y)

    # TODO: add magic methods such that two TwoDPoint objects can be added and subtracted coordinate-wise just by using
    #  syntax of the form p + q or p - q
    def __add__(self, other):
        if isinstance(other, TwoDPoint):
            return TwoDPoint(self.x + other.x, self.y + other.y)
        else:
            return TwoDPoint(0.0, 0.0)

    def __sub__(self, other):
        if isinstance(other, TwoDPoint):
            return TwoDPoint(self.x - other.x, self.y - other.y)
        else:
            return TwoDPoint(0.0, 0.0)

    @staticmethod
    def from_coordinates(coordinates: List[float]):
        if len(coordinates) % 2 != 0:
            raise Exception("Odd number of floats given to build a list of 2-d points")
        points = []
        it = iter(coordinates)
        for x in it:
            points.append(TwoDPoint(x, next(it)))
        return points

