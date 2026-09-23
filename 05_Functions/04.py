import math
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))
area, circumference = circle(radius)

print("Area of the circle is:", round(area, 2))
print("Circumference of the circle is:", round(circumference, 2))
