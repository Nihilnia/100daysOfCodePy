# for Loops

myList = [1,2,3,4,5,6,7,8,9]
total = 0
for f in myList:
    total += f
    print("{} is added to total.\nAnd total is {} now!".format(f, total),end = "\n\n")

print(". . .", end = "\n\n")
print("Loop is ended. And total result is:",total)


# Print even numbers.

myList2 = [1,2,3,4,5,6,7,8,9]
evenNumbers = list()

for numbers in myList2:
    if numbers % 2 == 0:
        evenNumbers.append(numbers)

print(*evenNumbers, sep = " - ")


# Another example

language = "Python"
numb = 0
for i in language:
    print(i, end=" is " + str(numb + 1)+".letter...\n")
    numb += 1


# AND the another

maList = [2352,15,124437,123424,12,3245324,153253]
yoNumbers = list()

for f in maList:
    if f % 2 == 0:
        yoNumbers.append(f)

yoNumbers.sort() #small to big
print(*yoNumbers)


# using for loops on tuples same like lists

maTuple = (1, 3, 4 ,5235, 21, 21.21)
for m in maTuple:
    print(m, end = " Maaa tuple\n")

# another example with tuples in a list

yayo = [(1, 2), ("nihil", "nia"), (0, "nhl")]
for skillZ in yayo:
    print(skillZ)
#as you can see we got tuples. And if you want we can call any value from them.
#Like this:
    print(skillZ[0])

#same like:
eyy = (["ayye", 12], [3333, 0])
newOne = list()
for s in eyy:
    newOne.append(s[1])
print(newOne)


#Actually we can get every value like this:

criminal = [(1, 0), ("nihil"," nia"), ("la", "rage")]
tupleNumber = 0
for x, y in criminal:
    numbbeer = 0
    tupleNumber += 1
    numbbeer += 1
    print("{0}.tuple's {1}.value {3} and {2}.Value {4}".format(tupleNumber, numbbeer, numbbeer + 1, x, y))


# But a little difference with dictionaries

myDict = {"a": 0, 1: "b", "c": 3}
for keys, values in myDict.items():
    print("Key: {}\tValue: {}".format(keys, values))