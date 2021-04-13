# Avish Parmar 112647892
from quadrilateral import Quadrilateral


class ShapeSorter:

    @staticmethod
    def sort(*args):
        a = []

        for arg in args:
            if isinstance(arg, Quadrilateral):
                a.append(arg)

        num = len(a)
        for i in range(num):
            for j in range(0, num - i - 1):
                if a[j].smallest_x() > a[j + 1].smallest_x():
                    a[j], a[j + 1] = a[j + 1], a[j]

        return a
