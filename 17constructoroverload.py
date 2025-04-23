class Rectangle:
    def __init__(self, length=None, width=None):
        if length and width:
            self.length = length
            self.width = width
        elif length:
            self.length = length
            self.width = length 
        else:
            self.length = 0
            self.width = 0
    
    def compute_area(self):
        return self.length * self.width

rect1 = Rectangle(5, 10) 
rect2 = Rectangle(5)  
rect3 = Rectangle()  

print("Area of rect1:", rect1.compute_area())
print("Area of rect2 (Square):", rect2.compute_area())
print("Area of rect3 (Default):", rect3.compute_area())
