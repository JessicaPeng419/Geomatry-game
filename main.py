from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fall_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.y \
        and rectangle.lowleft.x < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * \
               (self.upright.y - self.lowleft.y)

    def guess_off(self, guess):
        return abs(self.area() - guess)


if __name__ == '__main__':
    point1 = Point(10, 20)
    point2 = Point(5, 6)
    rect1 = Rectangle(
        Point(randint(0, 9), randint(0, 9)),
        Point(randint(5, 15), randint(5, 15)))

    print("The coordinator of the rectangle is: \n")
    print("Lower left: ", [rect1.lowleft.x, rect1.lowleft.y],
          ", Upper right: ", [rect1.upright.x, rect1.upright.y])
    usr_point = Point(float(input("Guess X: ")),
                      float(input("Guess Y: ")))
    print("Your point was inside the rectangle: ", usr_point.fall_in_rectangle(rect1))

    usr_area = float(input("Guess the area: "))
    print("The guess was ", rect1.guess_off(usr_area), " off from the right answer.")

