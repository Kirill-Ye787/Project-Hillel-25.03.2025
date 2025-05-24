class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути 0")
        self.a = a
        self.b = b
        self._normalize()

    def _normalize(self):
        # сокращение дроби
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        g = gcd(self.a, self.b)
        self.a //= g
        self.b //= g

    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"
