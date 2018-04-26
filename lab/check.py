a = 1
b = 970811
p = 320295887

y = 39639718
x = 0
# y**2 = x**3 + a*x + b (mod p)
s = (y * y) % p
t = (x * x * x + a * x + b) % p
u = (y * y - x * x * x - a * x - b) % p
print("s: " + str(s) + " t: " + str(t))
print(str(u))