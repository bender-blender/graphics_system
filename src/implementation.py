
# Реализации


class Color:
    """Цвет
    """
    def fill(self):
        raise NotImplementedError
    


class Blue(Color):
    """Синий

    Args:
        Color (_type_): _description_
    """
    def fill(self):
        return "Blue"
    

class Red(Color):
    """Красный

    Args:
        Color (_type_): _description_
    """
    def fill(self):
        return "Red"
