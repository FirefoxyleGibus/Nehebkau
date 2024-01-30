__all__ = [
    "Component"
    "Physics2D"
]

class Component:
    name = "Component"
    def __init__(self, gameObject = None):
        self.isActive = True
        self.gameObject = gameObject
        
    def SetActive(self, state):
        self.isActive = state
    
    def __str__(self):
        return f"{self.name} attached to {self.gameObject.name} : {self.isActive}"
    
    def Start(self):
        pass
    
    def Update(self, deltaTime):
        pass
    
    def OnDestroy(self):
        pass