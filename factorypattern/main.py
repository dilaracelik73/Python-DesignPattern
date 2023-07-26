import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width * self.width

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class ShapeFactory:
    def create_shape(self, name):
        if name == "circle":
            radius = float(input("Enter the radius of the circle, please: "))
            return Circle(radius)
        elif name == "rectangle":
            height = int(input("Enter the height of the rectangle, please: "))
            width = int(input("Enter the width of the rectangle, please: "))
            return Rectangle(height, width)
        elif name == "square":
            width = int(input("Enter the width of the square, please: "))
            return Square(width)

    @staticmethod
    def shapes_client():
        shape_factory = ShapeFactory()
        shape_name = input("Enter the name of the shape, please: ")
        shape = shape_factory.create_shape(shape_name)
        print(f"The type of object created: {type(shape)}")
        print(f"The area of the {shape_name} is: {shape.calculate_area()}")
        print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")


if __name__ == '__main__':
    ShapeFactory.shapes_client()
