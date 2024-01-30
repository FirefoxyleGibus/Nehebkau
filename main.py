import time
from decimal import Decimal, getcontext

from MathF.Vector import Vector2
from EngineObject.Scene import Scene
from EngineObject.GameObject import GameObject
from Component import Component
from Component import Physics2D

# @TODO
#   - Scene
#       - Delta Time
#   - Physics 2D
#       - Add Dynamic/Static Friction
#       - Add gravity Control
#       - Rotation ?
#       - Collision ?

getcontext().prec = 12

S = Scene()

A = S.AddGameObject("Light")
RigidA = Physics2D.Rigidbody2D(0.5, Vector2(0,0))
A.AddComponent(RigidA)
RigidA.AddForce(Vector2(2,1.5))

B = S.AddGameObject("Heavy")
RigidB = Physics2D.Rigidbody2D(2, Vector2(0,0))
B.AddComponent(RigidB)
RigidB.AddForce(Vector2(2,1.5))

C = S.AddGameObject("Control")
RigidC = Physics2D.Rigidbody2D(1, Vector2(0,0))
C.AddComponent(RigidC)
RigidC.AddForce(Vector2(2,1.5))


print("Light :", A.transform)
print("Heavy :", B.transform)
print("Control :", C.transform)

t = Decimal()

while (t < 2):
    t += Decimal(str(1/1000))
    print(f"\ntime = {t}")
    S.Update(Decimal(str(1/1000)))
    print("Light :", A.transform)
    print("Heavy :", B.transform)
    print("Control :", C.transform)