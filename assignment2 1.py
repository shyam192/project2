#assignment 2.1
#1 ans:
#methods of dictionaries
#1)clear() clear all the elements from
print("CLEAR()")
programs={"c":"easy","c++":"modarate","java":"tough"}

print("BEFORE CLEARING")
print(programs)

programs.clear()

print("AFTER CLEARING")
print(programs)

print("")
print("")
print("")

#2)copy() copy of the dictionarie
print("COPY()")
programs={"c":"easy","c++":"modarate","java":"tough"}
y=programs.copy()
print("After copying:")
print(y)

print("")
print("")
print("")

#3)fromkeys()
print("FROMKEYS")
programs={"c":"easy","c++":"modarate"}
y=("shyam",0)
mydict=programs.fromkeys(programs,y)
print(mydict)

print("")
print("")
print("")

#4)get()  return the value of the specified keys
print("GET FUNCTION")
programs={"c":"easy","c++":"modarate","java":"tough"}
x=programs.get("c")
print("value of c:")
print(x)

print("")
print("")
print("")

#5)items()  return the keys and values of a dictionaries in the form of tupple
print("items")
programs={"c":"easy","c++":"modarate","java":"tough"}
print(programs)
x=programs.items()
print(x)

print("")
print("")
print("")


#6)keys()  prints the dictionaries keys only
print("keys() function")
programs={"c":"easy","c++":"modarate","java":"tough"}
print(programs)
x=programs.keys()
print(x)

print("")
print("")
print("")


#7)pop remove the specified key from dictinaries
print("pop funtion")
programs={"c":"easy","c++":"modarate","java":"tough"}
print("before poping")
print(programs)
print("after poping")
programs.pop("c++")
print(programs)

print("")
print("")
print("")

#8)pop items remove the last inserted key-pair
print("pop items")
programs={"c":"easy","c++":"modarate","java":"tough"}
print("before poping")
print(programs)
print("after poping")
programs.popitem()
print(programs)

print("")
print("")
print("")

#9)setdefult()  add value to key or add a valu to any key
print("set defult case :")
programs={"c":"easy","c++":"modarate","java":"tough"}
print(programs)
x=programs.setdefault("c++","good")
print(x)


print("")
print("")
print("")






#QNO 2:

#SETS    unordered, unchangeable, and unindexed


#QNO 4

num=int(input("Enter the number of rows: "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
