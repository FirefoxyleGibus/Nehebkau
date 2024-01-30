from Component import Component
from MathF.Vector import Vector2
from decimal import Decimal

class Rigidbody2D(Component):
    name = "Rigidbody2D"
    def __init__(self, mass = Decimal(1), gravity = Vector2(0,-9.81)):
        super().__init__()
        if (type(mass) == Decimal):
            self.mass = mass
        elif (type(mass) == float) or (type(mass) == int):
            self.mass = Decimal(str(mass))
        else:
            raise TypeError("Expected value of type Decimal, float or int")
        self.velocity = Vector2(0,0) #vector
        self.acceleration = Vector2(0,0) #vector
        if (type(gravity) == Vector2):
            self.gravity = gravity
        else:
            raise TypeError("Expected value of type Vector2")
            
    def AddForce(self, force):
        """Add a force (as a Vector2) to the center of mass of the object following the formula F = ma"""
        self.velocity = force / self.mass
    
    def Update(self, deltaTime):
        vel = self.velocity
        self.velocity += (self.acceleration + self.gravity) * deltaTime
        self.gameObject.transform.position += (vel + self.velocity) * deltaTime * Decimal("0.5")
        