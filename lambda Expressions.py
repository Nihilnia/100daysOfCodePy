# let's remember list comprehensions.

listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [f * 2 for f in listOne if f % 2 == 0]

print(*listTwo)

# list comprehensions are much way pratic for create a list.
# like this, lambda expressions giving much more pratic way for create a function.
#watchThis:

# this is normal way to create a function

def exFunction(x):
    print(x * 2)

exFunction(35)

# now look:

exFunction2 = lambda x : print(x * 2)

exFunction2(35)

# for return, you don't need to write return, look

exFunction3 = lambda y : y * 3

print(exFunction3(3))

#another example:

exFunction4 = lambda x, y, z : x + y + z

print(exFunction4(2, 3, 4) * 2)

# and ofC another one

reverseString = lambda xStr : xStr[::-1]

print(reverseString("nihil"))

# yo another one'!

evenNumber = lambda number = int(input("give me a number")) : number % 2 == 0 
#this operation givin' us a boolean value.

if evenNumber():
    print("It's an even number.")
else:
    print("It's aint an even number.")


# all okay right? Simple

def topla(x, y, z):
    return x + y + z

print(topla(1, 2, 3))

toplax2 = lambda x, y, z : x + y + z

print(toplax2(4, 5, 6))

# last examples for now:

writeIT = lambda x = "nihil": print(x)

writeIT("ok")

#

writeREVERSE = lambda y : print(y[::-1])

writeREVERSE("tron")

#

xPrint = lambda *x : x
print(*xPrint("okan", 24))