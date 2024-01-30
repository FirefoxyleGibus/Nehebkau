from EngineObject.GameObject import GameObject, Transform
from MathF.Vector import Vector2

class Scene:
    def __init__(self, name = "Default", id = 0):
        self.name = name
        self.id = id
        self.idPointer = -1
        self.children = []
        
    def AddGameObject(self, name, transform = None):
        self.children.append(GameObject(name, self, transform))
        return self.children[-1]
           
    def GetID(self):
        while 1:
            self.idPointer += 1
            yield self.idPointer
    
    def Start():
        pass
    
    def Update(self, deltaTime):
        for child in self.children:
            child.Update(deltaTime)