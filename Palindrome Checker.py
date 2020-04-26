def palindrome (word):
    word = word.split(" ")

    if (len(word) > 1):
        for x in range(1,len(word)):
            word[0] += word[x]
        
        flip = word[0][::-1]

    else:
        flip = word[0][::-1]

    if(flip == word[0]):
        print("yes")

    else:
        print("no")
        

palindrome("nurses run")
#yes
palindrome("racecar")
#yes
palindrome("hello")
#no
