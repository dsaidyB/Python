import math

e = math.e
pi = math.pi

def add(a,b):
    result = a + b
    return result

def subtract(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result

def divide(a,b):
    if(b == 0):
        print("cannot divide by 0")
    else:
        result = a / b
        return result

def log(a,b):
    base = b
    result = math.log(a, base)
    return result

def power_of_y(a,b):
    result = a ** b
    return result

def log2(a):
    result = math.log2(a)
    return result

def log10(a):
    result = math.log10(a)
    return result

def ln(a):
    result = math.log(a)
    return result

def squared(a):
    result = a ** 2
    return result

def cubed(a):
    result = a ** 3
    return result

def sqrt(a):
    result = a ** 0.5
    return result

def sin(a):
    inputType = input("value in degrees or radians?")

    if (inputType == "degrees"):
        a = math.radians(a)

    result = math.sin(a)

    return result

def cos(a):
    inputType = input("value in degrees or radians?")

    if (inputType == "degrees"):
        a = math.radians(a)

    result = math.cos(a)

    return result

def tan(a):
    inputType = input("value in degrees or radians?")

    if (inputType == "degrees"):
        if(a == 90 or a == 270):
            print("error")
        else:
            a = math.radians(a)

    if (inputType == "radians"):
        if(a == pi/2 or pi == 3*pi/2):
            print("error")

    else:
        result = math.tan(a)
        return result



















def calculate (num1, num2, op):
    if (op == "+"):
        return add(num1, num2)

    elif (op == "-"):
        return subtract(num1, num2)

    elif (op == "x"):
        return multiply(num1, num2)

    elif (op == "/"):
        return divide(num1, num2)

    elif (op == "log"):
        return log(num1, num2)

    elif (op == "^y"):
        return power_of_y(num1, num2)













def calculate2 (op, val):

    if (op == "log2"):
        return log2(val)

    elif (op == "log10"):
        return log10(val)

    elif (op == "ln"):
        return ln(val)

    elif (op == "^2"):
        return squared(val)

    elif (op == "^3"):
        return cubed(val)

    elif (op == "sqrt"):
        return sqrt(val)

    elif (op == "sin"):
        return sin(val)

    elif (op == "cos"):
        return cos(val)

    elif (op == "tan"):
        return tan(val)

    else:
        print("error, enter different input")




print(calculate2("tan", pi/2))
