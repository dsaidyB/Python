def factorial(n):
    
    if (n < 0):
        print("number is not positive")
        
    #if isinstance(n,int):
    if (type(n) != int): 
        print("number is not an integer")
        
    else:
        result = 1
            
        for x in range(0,n):
            result = result * (n-x)
            
        print(result)
    
factorial(0)
