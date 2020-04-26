import math

e = math.e
pi = math.pi

def calculate (num1, num2, op):
    if (op == "+"):
        result = num1 + num2

    elif (op == "-"):
        result = num1 - num2

    elif (op == "x"):
        result = num1 * num2

    elif (op == "/"):
        result = num1 / num2

    elif (op == "log"):
        base = num2
        result = math.log(num1, base)

    elif (op == "^y"):
        result = num1 ** num2

    print(result)

def calculate2 (op, val):

    if (op == "log2"):
        result = math.log2(val)

    elif (op == "log10"):
        result = math.log10(val)

    elif (op == "ln"):
        result = math.log(val)

    elif (op == "^2"):
        result = val ** 2

    elif (op == "^3"):
        result = val ** 3

    elif (op == "sqrt"):
        result = math.sqrt(val)

    elif (op == "sin"):
        inputType = input("value in degrees or radians?")

        if (inputType == "degrees"):
            val = math.radians(val)

        result = math.sin(val)

    elif (op == "cos"):
        inputType = input("value in degrees or radians?")

        if (inputType == "degrees"):
            val = math.radians(val)

        result = math.cos(val)

    elif (op == "tan"):
        inputType = input("value in degrees or radians?")

        if (inputType == "degrees"):
            if(val == 90 or val == 270):
                print("error")
            else:
                val = math.radians(val)

        result = math.tan(val)

    else:
        print("error")

    print(result)
