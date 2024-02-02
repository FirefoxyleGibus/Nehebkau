import mpmath
from mpmath import *
import math

class Vector2():
    # Static functions
    def dot(v1, v2):
        return (v1.x * v2.x) + (v1.y * v2.y)
    
    def angle(v1, v2):
        return acos(Vector2.dot(v1, v2))
    
    def defineAmpl(amplitude, angle):
        return Vector2(cos(angle) * amplitude, sin(angle) * amplitude)
    
    # Instance functions
    def __init__(self, x, y): # Decimal
        self.x = mpmathify(x)
        self.y = mpmathify(y)
    
    def __add__(self, o):
        if (type(o) == Vector2):
            return Vector2(self.x + o.x, self.y + o.y)
        
    def __sub__(self, o):
        if (type(o) == Vector2):
            return Vector2(self.x - o.x, self.y - o.y)
    
    def __mul__(self, o):
        if (type(o) == mpmath.ctx_mp_python.mpf):
            return Vector2(self.x * o, self.y * o)
    
    def  __truediv__(self, o):
        if (type(o) == mpmath.ctx_mp_python.mpf):
            return Vector2(self.x / o, self.y / o)
    
    def __pow__(self, o):
        if (type(o) == mpmath.ctx_mp_python.mpf):
            return Vector2(self.x ** o, self.y ** o)
    
    def __str__(self):
        return f"{self.x}; {self.y}"
    
    def amplitude(self):
        return (self.x + self.y).sqrt()
    
    def normalize(self):
        ampl = self.amplitude()
        return Vector2(self.x / ampl, self.y / ampl)
    
    def angleToWorld(self):
        return Vector2.angle(Vector2(0,1), self)