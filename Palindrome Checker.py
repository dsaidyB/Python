def palindrome (word):
    word = word.split(" ")
    #print(word)
    
    if (len(word) > 1):
        for x in range(1,len(word),2):
            hey = word[x-1] + word[x] 
        
        flip = hey[::-1]

    else:
        flip = word[0][::-1]
    
    if(flip == word[0]):
        print("yes")
        
    else:
        print("no")
        
    #print(word)    
    #print(flip)
    
palindrome("nurses run")
palindrome(“racecar”)
palindrome(“hello”)
