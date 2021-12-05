import math

a = {'l': 1, 'r': 5, 'u': 3, 'd': math.inf}
print(min(a, key=a.get))
