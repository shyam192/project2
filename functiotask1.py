#decreasing order frequency
def most_frequent(string):          #function prototype
    d1 = dict() 
    for letter in string:
        if letter in d1:            #searching character in dctionary
            d1[letter]=d1[letter]+1

        else:
            d1[letter]=1

    return dict(sorted(d1.items(),key=lambda t:t[1],reverse=True))
    

x=input("Please enter the string:")
print(most_frequent(x))

