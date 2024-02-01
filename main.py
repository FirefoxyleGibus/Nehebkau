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
RigidA = Physics2D.Rigidbody2D(0.5, Vector2(0,-9.81))
A.AddComponent(RigidA)
RigidA.AddForce(Vector2(2,1.5))

B = S.AddGameObject("Heavy")
RigidB = Physics2D.Rigidbody2D(2, Vector2(0,-9.81))
B.AddComponent(RigidB)
RigidB.AddForce(Vector2(2,1.5))

C = S.AddGameObject("Control")
RigidC = Physics2D.Rigidbody2D(1, Vector2(0,-9.81))
C.AddComponent(RigidC)
RigidC.AddForce(Vector2(2,1.5))


print("Light :", A.transform)
print("Heavy :", B.transform)
print("Control :", C.transform)

tStart = time.perf_counter()
t1 = time.perf_counter()
t2 = time.perf_counter()

avgTime = 0
frames = 0

testTime = 10

framerateCap = 1/60

while(time.perf_counter() - t2 < framerateCap):
    pass

while ((t2 - tStart) < 10):
    t2 = time.perf_counter()
    frames += 1
    avgTime += t2 - t1
    print(f"\nReal Time = {t2 - tStart}\nFrame Time : {t2 - t1}\nFrame : {frames}\nAVG Frame time : {avgTime / frames}")
    S.Update(Decimal(str(t2)) - Decimal(str(t1)))
    print("Light\t:", A.transform)
    print("Heavy\t:", B.transform)
    print("Control\t:", C.transform)
    while(time.perf_counter() - t2 < framerateCap):
        pass
    t1 = t2

print(f"\n================\nTest completed !\nAverage frames / s\t\t: {frames / 10}\nAverage frame time\t\t: {avgTime/frames}\nEstimated frames / s\t: {frames/avgTime}")
input()