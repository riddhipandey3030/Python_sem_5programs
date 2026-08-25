#Create a class shape with variable radius.Initialize the variable with constructor.
#Create a class circle which is the child class of shape class.Define a method cal_Area()
#to calculate the area of circle using math package. Create a class sphere which is a child class
#of shape class. Define Cal_Volume() to calculate the volume of sphere.
#---------------------------------------------------------------------------------------------------
import math
class Shape:
    def __init__(self,radius):
        self.radius=radius
class Circle(Shape):
    def Cal_Area(self):
        area=math.pi* pow(self.radius,2)
        print("Area of circle: ",area)
class Sphere(Shape):
    def Cal_Volume(self):
        vol=(4/3) * math.pi * pow(self.radius, 3)
        print("Volume of Sphere =", vol)
c=Circle(5)
c.Cal_Area()
s=Sphere(6)
s.Cal_Volume()
