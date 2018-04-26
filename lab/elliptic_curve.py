from time import gmtime, strftime, time
# y**2 = x**3 + a*x + b
import copy

a = 1
b = 50741573

p = 88176923

class Point:
    x = 0
    y = 0
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy
    def __repr__(self):
        return "Point()"
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __ne__(self, other):
        return not self == other

def check():
    if (4*a**3 + 27*b**2) % p == 0:
        print("Not an elliptic curve, choose another a and b")
        exit(-1)

points_of_curve = []

def extended_euclidean_algorithm(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t

def inverse_mod(k):
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - inverse_mod(-k)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    gcd, x, y = old_r, old_s, old_t
    assert gcd == 1
    assert (k * x) % p == 1
    return x % p

def belong(point):
    if point == Point(0,0):
        return True
    if (point.y**2) % p == (point.x**3 + a*point.x + b) % p:
        return True
    else:
        return False

def build():
    check()
    for i in range(0, p):
        for j in range(0, p):
            pt = Point(i,j)
            bl = belong(pt)
            if bl:
                points_of_curve.append(pt)
            if len(points_of_curve) > 2:
                break

def addition(pp, qq):
    if pp == Point(0,0):
        return qq
    if qq == Point(0,0):
        return pp
    if pp.x == qq.x and pp.y != qq.y:
        return Point(0,0)
    if (pp == qq):
        m = ((3 * pp.x * pp.x + a) * inverse_mod(2 * pp.y)) % p
    else:
        m = ((pp.y - qq.y) * inverse_mod(pp.x - qq.x)) % p
    x = (m * m - pp.x - qq.x) % p
    y = (pp.y + m * (x - pp.x)) % p
    return Point(x, -y%p)

def find(point):
    k = 0
    sum = copy.copy(point)
    sum = addition(sum, point)
    while (sum != point):
        k = k + 1
        sum = addition(sum, point)
        # print(str(sum) + " " + str(belong(sum)))
    print("find: ")
    print(str(sum))
    print("k: " + str(k))

p1 = Point(78509055, 39207340)
if belong(p1):
    print("Appropriate point")
    t1 = time()
    find(p1)
    t2 = time()
    print("Time=%s" % (t2 - t1))
else:
    print("Point doesn't belong to curve, choose another one")
    build()
    for i in points_of_curve:
        print(str(i))

# s = (39639718 * 39639718) % p
# t = b % p
# y = 39639718
# x = 0
# u = (y * y - x * x * x - a * x - b) % p
# print("s: " + str(s) + ", t: " + str(t))
# print(str(u))