def hypotenuse(sidea, sideb):
    c = int((sidea**2 + sideb**2) ** 0.5)
    print(c)

def side_length(sidea, hypot):
    b = int((hypot**2 - sidea**2) ** 0.5)
    print(b)

hypotenuse(3,4)
#output 5
side_length(5,13)
#output 12
