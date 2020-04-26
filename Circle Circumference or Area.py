import math

pi = math.pi

def area (r):
    result = pi * (r**2)
    #print(result)
    return result

def circum (r):
    result = 2*pi*r
    return result
    #print(result)

# area(3)
# circum(3)

print(area(3))
