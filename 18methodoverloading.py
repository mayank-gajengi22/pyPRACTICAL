class Shape:
    def area(self, side=None, length=None, breadth=None):
        if side is not None:
            return side * side  
        elif length is not None and breadth is not None:
            return length * breadth  
        else:
            return "Insufficient parameters"


shape = Shape()


print("Area of square:", shape.area(4))  


print("Area of rectangle:", shape.area(length=5, breadth=10))  
