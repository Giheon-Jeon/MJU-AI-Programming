import numpy as np

a = np.arange(0, 10, 2)
b = np.arange(12)
c = np.linspace(0, 1, 5)
d = np.linspace(0, 2*3.14159, 100)
e = np.array([1.2, 3.7, -2.4]).astype(int)

print(a) # [0 2 4 6 8]
print(b)
print(c) # [0. 0.25 0.5 0.75 1. ]
print(d)
print(e) # [ 1 3 -2]
