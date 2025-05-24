class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        total_area = self.get_square() + other.get_square()
        # пусть новая ширина = текущая ширина, высота подбирается автоматически
        new_width = self.width
        new_height = total_area // new_width
        while new_width * new_height != total_area:
            new_width += 1
            new_height = total_area // new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError("Множення можливе тільки на число")
        new_area = self.get_square() * n
        new_width = self.width
        new_height = int(new_area // new_width)
        while new_width * new_height != new_area:
            new_width += 1
            new_height = int(new_area // new_width)
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
