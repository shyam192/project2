#FIBONACCI SERIES
no_terms=int(input("ENTER THE NUMBER(how many terms?)"))    #upto what terms to print fibonacci series

i=0
j=1
            #checking the input number
if no_terms<=0:
    print("wrong:you enter a negative number")
    print("please enter positive number")
else:
    print("FIBONACCI SERIES:")
    while i<no_terms:  #printing series
        k=i+j
        print(k)
        i=j
        j=k
