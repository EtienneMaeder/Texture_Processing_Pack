class Vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return

    def add(self, Vec3):
        self.x += Vec3.x
        self.y += Vec3.y
        self.z += Vec3.z
        return