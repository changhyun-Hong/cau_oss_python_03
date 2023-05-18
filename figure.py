import math

# figure 모듈은 line클래스와 3개의 함수를 갖고 있다

# line 클래스는 length를 0으로 초기화하고 getter함수와 setter함수를 갖고 있다


class line:

    __length = 0
    
    def __init__(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length


# area_square 함수는 사각형의 넓이를 구하는 함수이다
def area_square(length):
    return length * length

# area_circle 함수는 원의 넓이를 구하는 함수이다
def area_circle(length):
    return length * length * math.pi

# area_regular_triangle 함수는 정삼각형의 넓이를 구하는 함수이다
def area_regular_triangle(length):
    return length * length * math.sqrt(3) / 4
