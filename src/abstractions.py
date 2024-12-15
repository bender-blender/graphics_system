from abc import ABC, abstractmethod


# Абстракция

class Shape(ABC):
    """Фигура

    Args:
        ABC (_type_): _description_
    """
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def draw(self):
        raise NotImplementedError