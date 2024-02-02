import time

from mpmath import mpmathify

from MathF.Vector import Vector2
from EngineObject.Scene import Scene
from EngineObject.GameObject import GameObject
from Component import Component
from Component import Physics2D

# @TODO
#   - Physics 2D
#       - Add gravity Control
#       - Rotation ?
#       - Collision ?

S = Scene()

A = S.AddGameObject("Light")
RigidA = Physics2D.Rigidbody2D(5, Vector2(0,0), 0.05)
A.AddComponent(RigidA)
RigidA.AddForce(Vector2(2,1.5))

B = S.AddGameObject("Heavy")
RigidB = Physics2D.Rigidbody2D(20, Vector2(0,0), 0.2)
B.AddComponent(RigidB)
RigidB.AddForce(Vector2(2,1.5))

C = S.AddGameObject("Control")
RigidC = Physics2D.Rigidbody2D(10, Vector2(0,0), 0.1)
C.AddComponent(RigidC)
RigidC.AddForce(Vector2(2,1.5))


print("Light :", A.transform)
print("Heavy :", B.transform)
print("Control :", C.transform)

tStart = time.perf_counter()
t1 = mpmathify(time.perf_counter())
t2 = mpmathify(time.perf_counter())

avgTime = 0
frames = 0

testTime = 10

framerateCap = mpmathify(1/60)

while(time.perf_counter() - t2 < framerateCap):
    pass

while ((t2 - tStart) < testTime):
    t2 = time.perf_counter()
    frames += 1
    avgTime += t2 - t1
    print(f"\nReal Time = {t2 - tStart}\nFrame Time : {t2 - t1}\nFrame : {frames}\nAVG Frame time : {avgTime / frames}")
    S.Update(mpmathify(t2) - mpmathify(t1))
    print("Light\t:", A.transform)
    print("Heavy\t:", B.transform)
    print("Control\t:", C.transform)
    while(time.perf_counter() - t2 < framerateCap):
        pass
    t1 = t2

print(f"\n================\nTest completed !\nAverage frames / s : {frames / testTime}\nAverage frame time : {avgTime/frames}\nEstimated frames / s : {frames/avgTime}")
input()