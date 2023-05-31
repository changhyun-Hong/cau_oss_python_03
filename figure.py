import math

# figure 모듈은 line클래스와 3개의 함수를 갖고 있다
# line 클래스는 width와 height를 0으로 초기화하고 getter함수와 setter함수를 갖고 있다


class line:

    __width = 0
    __height = 0

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_length(self):
        return self.__width, self.__height

    def set_length(self, width, height):
        self.__width = width
        self.__height = height


# area_srectangular 함수는 직사각형의 넓이를 구하는 함수이다
def area_rectangular(width, height):
    if width <= 0 or height <= 0:
        raise ValueError
    return width * height

# area_ellipse 함수는 타원의 넓이를 구하는 함수이다


def area_ellipse(width, height):
    if width <= 0 or height <= 0:
        raise ValueError
    return width * height * math.pi

# area_right_triangle 함수는 직각삼각형의 넓이를 구하는 함수이다


def area_right_triangle(width, height):
    if width <= 0 or height <= 0:
        raise ValueError
    return width * height / 2
