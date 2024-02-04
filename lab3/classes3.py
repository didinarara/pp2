class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0 

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

shape_obj = Shape()
print("Area of the shape:", shape_obj.area())

square_obj = Square(5)
print("Area of the square:", square_obj.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle_obj = Rectangle(4, 6)
print("Area of the rectangle:", rectangle_obj.area())
