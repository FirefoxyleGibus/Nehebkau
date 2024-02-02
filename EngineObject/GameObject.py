from Component import Component
from MathF.Vector import Vector2
from mpmath import *

class GameObject:
    def __init__(self, name, parent, transform = None):
        self.name = str(name)
        self.parent = parent     
        self.id         = self.GetID()
        self.isActive   = True
        self.children   = []
        if (transform == None):
            self.transform = Transform(gameObject = self)
        elif (type(transform) == Transform):
            self.transform  = transform
        else:
            raise TypeError("Expected value of type Transform")
        self.component  = {"Transform": self.transform}
    
    def SetActive(self, state):
        self.isActive = state
    
    def GetID(self):
        self.parent.GetID()
    
    def AddChild(self, name, transform = None):
        self.children.append(GameObject(name, self, transform))
        return self.children[-1]
        
    def AddComponent(self, component):
        """
        component : Component (and subclasses)
        
        Takes a Component and adds it to the component dict, If multiple component gets added, the name will be ComponentType + number starting at 1
        """
        if (issubclass(type(component), Component)):
            self.component[ApplyName(self.component,component.name)] = component
            component.gameObject = self
        else:
            print("no no")
            pass
        
    def GetComponent(self, compName):
        """
        compName : string
        
        Returns the component with name compName (usually the component type)
        """
        return self.component.get(compName)
    
    def DeleteComponent(self, compName):
        """
        compName : string
        
        Deletes the component with name compName (usually the component type)
        """
        self.component.pop(compName)
    
    def Start(self):
        pass
    
    def Update(self, deltaTime):
        if (self.isActive):
            for comp in self.component.keys():
                if (self.component[comp].isActive):
                    self.component[comp].Update(deltaTime)
            for child in self.children:
                child.Update(deltaTime)
    
    def OnDestroy(self):
        pass

class Transform(Component):
    name = "Transform"
    def __init__(self, position = Vector2(0, 0), rotation = mp.mpf(), gameObject = None):
        super().__init__(gameObject)
        if (type(position) == Vector2):
            self.position = position
        else:
            raise TypeError("Expected value of type Vector2")
            
        self.rotation = mpmathify(rotation)
        
        self.up = Vector2.defineAmpl(1, self.rotation)
        self.right = Vector2.defineAmpl(1, self.rotation + 90)
    
    def __str__(self):
        return f"Transform comp : {self.position.x} {self.position.y}"
        
        
def ApplyName(dictionnary, itemName):
    count = 1
    if (itemName in dictionnary):
        while (1):
            newItemName = itemName + str(count)
            if (newItemName  not in dictionnary):
                return newItemName
            count += 1
    return itemName