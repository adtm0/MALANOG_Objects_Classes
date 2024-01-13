import math

class Circle:
    
    def __init__(self):
        self.radius = int(input("Enter a radius: "))
        self.pi = math.pi
        
    def area(self):
        print(f"Area of the Circle is {(math.pi * (self.radius ** 2)).__round__(2)}")
        
    def perimeter(self):
        print(f"Circumference of the Circle is {(2 * math.pi * self.radius).__round__(2)}")

c = Circle()
c.area()
c.perimeter()