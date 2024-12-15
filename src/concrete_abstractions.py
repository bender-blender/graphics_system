from abstractions import Shape
from implementation import (
    Color,
    Red,
    Blue
    )


class Circle(Shape):
    """Круг

    Args:
        Shape (_type_): _description_
    """
    def __init__(self, color: Color):
        self.color = color
        super().__init__(color)

    def draw(self):
        return f"Нарисован круг цвета {self.color.fill()}"
    

class Square(Shape):
    """Квадрат

    Args:
        Shape (_type_): _description_
    """
    def __init__(self, color: Color):
        self.color = color
        super().__init__(color)

    def draw(self):
        return f"Нарисован квадрат цвета {self.color.fill()}"
    

if __name__ == "__main__":
    red_circle = Circle(Red())
    blue_square = Square(Blue())

    print(red_circle.draw())  
    print(blue_square.draw()) 