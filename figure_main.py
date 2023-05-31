# import를 통해 figure 모듈을 호출한다
import figure

myline = figure.line(10, 20)
width, height = myline.get_length()

try:
    rectangle = figure.area_rectangle(width, height)
    ellipse = figure.area_ellipse(width, height)
    right_triangle = figure.area_right_triangle(width, height)
    print(rectangle)
    print(ellipse)
    print(right_triangle)
except ValueError:
    print("Please input positive number for width and height")
