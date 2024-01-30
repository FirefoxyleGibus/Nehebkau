from decimal import Decimal

class Vector2():
    def __init__(self, x, y): # Decimal
        if (type(x) == Decimal):
            self.x = x
        elif (type(x) == float) or (type(x) == int):
            self.x = Decimal(str(x))
        else:
            raise TypeError("Expected value of type Decimal, float or int")
        if (type(y) == Decimal):
            self.y = y
        elif (type(y) == float) or (type(y) == int):
            self.y = Decimal(str(y))
        else:
            raise TypeError("Expected value of type Decimal, float or int")
    
    def __add__(self, o):
        if (type(o) == Vector2):
            return Vector2(self.x + o.x, self.y + o.y) 
    
    def __mul__(self, o):
        if (type(o) == Decimal):
            return Vector2(self.x * o, self.y * o)
    
    def  __truediv__(self, o):
        if (type(o) == Decimal):
            return Vector2(self.x / o, self.y / o)
    
    def __pow__(self, o):
        if (type(o) == Decimal):
            return Vector2(self.x ** o, self.y ** o)
    
    def __str__(self):
        return f"{self.x}; {self.y}"