#Create a class Triangle with 3 variables side1,side2,side3. Initialize the variables with 
# constructor.It also has the variables angle1,angle2,angle3.Create a class equivalent triangle
# and find the area of triangle with Cal_Area() function. Find the tangent of all angles using
# find_angle() function.Create a class Scalene which is a child of Triangle class. 
# Find out the perimeter of triangle with Cal_Perimeter() function. Find out the area of triangle 
# with Cal_Area() function. Use the math package for the computation. Print the area as a 
# whole no. and not a decimal.
#-------------------------------------------------------------------------------------------
import math
class Triangle:
    def __init__(self,side1,side2,side3,angle1,angle2,angle3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
class Equivalent(Triangle):
    def Cal_Area(self):
        area = (math.sqrt(3) / 4) * pow(self.side1, 2)
        print("Area of Equivalent Triangle =", round(area))
    def find_Angle(self):
        print("Tan of angle 1 =", math.tan(math.radians(self.angle1)))
        print("Tan of angle 2 =", math.tan(math.radians(self.angle2)))
        print("Tan of angle 3 =", math.tan(math.radians(self.angle3)))
class Scalene(Triangle):
    def Cal_Perimeter(self):
        perimeter=self.side1+self.side2+self.side3
        print("Perimeter of Scalene Triangle is: ",perimeter)
        
    def Cal_Area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s-self.side1) * (s-self.side2) * (s-self.side3))
        print("Area of Scalene Triangle =", int(area))
e=Equivalent(8,8,8,60,60,60)
e.Cal_Area()
e.find_Angle()
s=Scalene(6,8,4,30,45,60)
s.Cal_Perimeter()
s.Cal_Area()


