# # fast example

number = 0
while (number <= 22):
    print("Number: ",number)
    number += 2
print("\n. . .\n\nLoop Ended!")

# another one

key = 0
while key < 40:
    key += 1
    print("I am learning Python!", key)

# using while Loop with a list

myList = ["nihil", 2, "24", 4, 5]
indexNumber = 0
while indexNumber < len(myList):
    print("Index number: ", indexNumber,"\nitem: ", myList[indexNumber], end="\n\n")
    indexNumber += 1

# and OF COURSE WE HAVE INFINITE LOOPS!
# if condition of loop wouldn't be False, loop would work endless.
# let's make it with same example:

myList = ["nihil", 2, "24", 4, 5]
indexNumber = 0
while indexNumber < len(myList):
    print("Index number: ", indexNumber,"\nitem: ", myList[indexNumber], end="\n\n")
    # indexNumber += 1 - Now, loop will never end