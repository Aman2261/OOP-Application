import math

# 2D VECTOR

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # print the vector
    def __str__(self):
        return f"({self.x}, {self.y})"

    # v1 + v2
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # v1 - v2
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # v * scalar
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    # v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # magnitude (length of vector)
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    # dot product: a.b = ax*bx + ay*by
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # angle between two vectors (in degrees)
    def angle_with(self, other):
        cos_angle = self.dot(other) / (self.magnitude() * other.magnitude())
        cos_angle = max(-1, min(1, cos_angle))   # clamp to avoid float errors
        return math.degrees(math.acos(cos_angle))

    # unit vector (same direction, length = 1)
    def normalize(self):
        mag = self.magnitude()
        return Vector2D(self.x / mag, self.y / mag)

    # note: no cross product in 2D (returns a scalar, not a vector)
    def cross(self, other):
        return self.x * other.y - self.y * other.x


#  3D VECTOR

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # print the vector
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # v1 + v2
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # v1 - v2
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    # v * scalar
    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    # v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # magnitude (length of vector)
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # dot product: a.b = ax*bx + ay*by + az*bz
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # cross product: returns a new vector perpendicular to both
    def cross(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

    # angle between two vectors (in degrees)
    def angle_with(self, other):
        cos_angle = self.dot(other) / (self.magnitude() * other.magnitude())
        cos_angle = max(-1, min(1, cos_angle))
        return math.degrees(math.acos(cos_angle))

    # unit vector (same direction, length = 1)
    def normalize(self):
        mag = self.magnitude()
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)


#  DEMO

print("=" * 40)
print("        2D VECTOR DEMO")
print("=" * 40)

a = Vector2D(3, 4)
b = Vector2D(1, 2)

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * 3 = {a * 3}")
print(f"magnitude of a = {a.magnitude()}")
print(f"dot product = {a.dot(b)}")
print(f"cross product (scalar) = {a.cross(b)}")
print(f"angle between a and b = {a.angle_with(b):.2f} degrees")
print(f"normalize a = {a.normalize()}")
print(f"a == b: {a == b}")
print(f"a == a: {a == a}")

print()
print("=" * 40)
print("        3D VECTOR DEMO")
print("=" * 40)

u = Vector3D(1, 2, 3)
v = Vector3D(4, 5, 6)

print(f"u = {u}")
print(f"v = {v}")
print(f"u + v = {u + v}")
print(f"u - v = {u - v}")
print(f"u * 2 = {u * 2}")
print(f"magnitude of u = {u.magnitude():.2f}")
print(f"dot product = {u.dot(v)}")
print(f"cross product = {u.cross(v)}")
print(f"angle between u and v = {u.angle_with(v):.2f} degrees")
print(f"normalize u = {u.normalize()}")
print(f"u == v: {u == v}")
print(f"u == u: {u == u}")
