from Component import Component
from MathF.Vector import Vector2
from mpmath import *

class Rigidbody2D(Component):
    name = "Rigidbody2D"
    def __init__(self, mass = mp.mpf(1), gravity = Vector2(0,-9.81), dynamicFriction = mp.mpf(0.1), staticFriction = mp.mpf(0.1)):
        super().__init__()
        self.mass = mpmathify(mass)
        self.velocity = Vector2(0,0) #vector
        self.acceleration = Vector2(0,0) #vector
        if (type(gravity) == Vector2):
            self.gravity = gravity
        else:
            raise TypeError("Expected value of type Vector2")
        self.dynamicFriction = mpmathify(dynamicFriction)
        self.staticFriction = mpmathify(staticFriction)
            
    def AddForce(self, force):
        """Add a force (as a Vector2) to the center of mass of the object following the formula F = ma"""
        if (force.amplitude() > self.staticFriction * self.mass):
            self.velocity = force / self.mass
    
    def Update(self, deltaTime):
        vel = self.velocity
        self.velocity += (self.acceleration + self.gravity) * deltaTime - vel * self.dynamicFriction
        self.gameObject.transform.position += (vel + self.velocity) * deltaTime * mp.mpf("0.5")
        