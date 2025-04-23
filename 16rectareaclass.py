class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width

rect = Rectangle(5, 10)
print("The area of the rectangle is:", rect.compute_area())
