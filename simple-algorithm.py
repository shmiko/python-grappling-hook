import sys
import Math

def time(a):
    return 3 + 2 * a

def naive(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z
# result = naive()
print(naive(2,5))
