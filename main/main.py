import TestModule.Math as math

one = math.Vec3(1, 2, 3)
two = math.Vec3(2, 3, 4)

print(one.x, one.y, one.z)
one.add(two)
print(one.x, one.y, one.z)

