# Develop an inheritance hierarchy based upon a Polygon class that has
#  abstract methods area() and perimeter(). Implement classes Triangle,
#  Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
#  class, with the obvious meanings for the area() and perimeter() methods.
#  Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle,
# and Square, that have the appropriate inheritance relationships. Finally,
#  write a simple program that allows users to create polygons of the
#  various types and input their geometric dimensions, and the program then
#  outputs their area and perimeter. For extra effort, allow users to input
#  polygons by specifying their vertex coordinates and be able to test if two
#  such polygons are similar.
import math
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Polygon):
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("不符合三角形边长")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    def area(self):
        p = self.perimeter() / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s


class IsoscelesTriangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a, b, b)


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


# 此部分代码只考虑了有外接圆的四边形
class Quadrilateral(Polygon):
    def __init__(self, a, b, c, d):
        if not (a + b == c + d or a + c == b + d or a + d == b + c):
            raise ValueError("不符合四边形边长")
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        p = self.a + self.b + self.c + self.d
        return p

    def area(self):
        p = self.perimeter() / 2
        s = math.sqrt((p - self.a) * (p - self.b) * (p - self.c) * (p - self.d))
        return s


class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)


class Square(Quadrilateral):
    def __init__(self, length):
        super().__init__(length, length, length, length)


class RegularPolygon(Polygon):
    def __init__(self, side, length):
        self.side = side
        self.length = length

    def perimeter(self):
        return self.side * self.length

    def area(self):
        return (self.side * self.length ** 2) / (4 * math.tan(math.pi / self.side))


class Pentagon(RegularPolygon):
    def __init__(self, length):
        super().__init__(5, length)


class Hexagon(RegularPolygon):
    def __init__(self, length):
        super().__init__(6, length)


class Octagon(RegularPolygon):
    def __init__(self, length):
        super().__init__(8, length)


def create_polygon():
    print("选择多边形类型：")
    print("1. 三角形  2. 等腰三角形  3. 等边三角形")
    print("4. 四边形  5.矩形  6. 正方形")
    print("7. 正五边形  8. 正六边形  9. 正八边形")
    choice = input("请输入选择（1-9）：")

    if choice == '1':
        a = float(input("边1："))
        b = float(input("边2："))
        c = float(input("边3："))
        return Triangle(a, b, c)
    elif choice == '2':
        base = float(input("底边："))
        side = float(input("腰长："))
        return IsoscelesTriangle(base, side)
    elif choice == '3':
        side = float(input("边长："))
        return EquilateralTriangle(side)
    elif choice == '4':
        a = float(input("边1："))
        b = float(input("边2："))
        c = float(input("边3："))
        d = float(input("边4："))
        return Quadrilateral(a, b, c, d)
    elif choice == '5':
        l = float(input("长："))
        w = float(input("宽："))
        return Rectangle(l, w)
    elif choice == '6':
        s = float(input("边长："))
        return Square(s)
    elif choice == '7':
        s = float(input("边长："))
        return Pentagon(s)
    elif choice == '8':
        s = float(input("边长："))
        return Hexagon(s)
    elif choice == '9':
        s = float(input("边长："))
        return Octagon(s)
    else:
        raise ValueError("无效选择")


if __name__ == "__main__":
    poly1 = create_polygon()
    print(f"\n多边形面积：{poly1.area():.2f} 周长：{poly1.perimeter():.2f}")
