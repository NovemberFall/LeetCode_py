class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other):
        if self.a < other.a:
            return True
        elif self.a == other.a and self.b < other.b:
            return True
        elif self.a == other.a and self.b == other.b and self.c < other.c:
            return True
        else:
            return False 