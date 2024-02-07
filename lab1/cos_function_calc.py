import math

x = 3.8
while x <= 7.6:
    y = (math.cos(x) ** 2) / (x**2 + 1)
    print(f"x: {x}, y: {y}")  
    x += 0.6
