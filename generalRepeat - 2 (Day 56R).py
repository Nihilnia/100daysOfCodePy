#Input()
# Just do not forget, everything is String is what is coming with input.

#### Logical Values And Operands ####

# - Boolean Values

#True And False

a = True
print(type(a))
#<class 'bool'>

#NOTE: If a value is not zero or empty, it's True
#example:

b = 0
print(type(b))
#<class 'int'>
print(bool(b))
#False

c = None
print(bool(c))
#False

#None?
# If you don't wanna give any value to a Variable, you can create the variable and you can give None
#Anytime you can change.

#Comparison Operands
#We know all about that.

#### IF - ELSE CONTROL Statements
#We know all about that.
# Just be careful when you create blocks.
# Be logical!

#### LOOPS - For and While ####
#We know all about that.
# Be logical!

# Let's create a basic loop
# Even number picker.

numbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for numbers in numbersList:
    if numbers % 2 == 0:
        print(numbers)


#Quick tip!
# Using For loops is same for strings, lists, tuples.
# And of course except 'some exceptional status'.

# Quick tip!
#While you create a for loop, be careful, be logical.
# Example:

exampleDict = {"firstKey": "firstValue", "secondKey": "secondValue", "thirdKey": "thirdValue"}
#here is we have keys and values.
# So we need two variable while creating loop, watch it:

allKeys = list()
allValues = list()
for keys, values in exampleDict.items():
    allKeys.append(keys)
    allValues.append(values)

print("Here is the keys:")
print(*allKeys, sep = ", ", end = ".\n\n")
print("Here is the values:")
print(*allValues, sep = ", ", end = ".")

#let's say we want to get ONLY VALUES

yaValues = list()
for xValues in exampleDict.values():
    yaValues.append(xValues)
print(*yaValues)

#LET'S SAY WE HAVE A LISTS IN A LIST

ghost = [[1, 2, 3], ["4", "5", "6"], [7, 8, 9]]
#let's do this.

firstList = list()
secondList = list()
thirdList = list()

key = 0
for lists in ghost:
    key += 1

    if key == 1:
        firstList.append(lists)

    elif key == 2:
        secondList.append(lists)
    
    else:
        thirdList.append(lists)

print("First list:", firstList)
print("Second list:", secondList)
print("Third list:", thirdList)

# or do it like that, watch it:

secondGhost = [[1, 2, 3], ["4", "5", "6"], [7, 8, 9]]
for secondLists in secondGhost:
    for deep in secondLists:
        print(deep, ":", type(deep))

# or do it just for fun:

secondGhost = [[1, 2, 3], ["4", "5", "6"], [7, 8, 9]]
for secondLists in secondGhost:
    for deep in secondLists:
        if type(deep) == type(int):
            print(deep, ":", "integer!")
        elif type(deep) == type(str):
            print(deep, ":", "string!")
        
# make categorize

#Type Comparison

allStringsInList = list()
allIntegersInList = list()

secondGhost = [[1, 2, 3], ["4", "5", "6"], [7, 8, 9]]

for secondLists in secondGhost:
    for items in secondLists:
        if isinstance(items, int):
            allIntegersInList.append(items)
        elif isinstance(items, str):
            allStringsInList.append(items)

print("All integer in the list:", *allIntegersInList, sep = ", ", end = ".\n\n")
print("All strings in the list:", *allStringsInList, sep = ", ", end = ".\n\n")


#### While Loops #####
# We know but let's make a example:

#Lottery Number Generator

import random

numbers = list()
key = 1

while key != 11:
    randomNumber = random.randint(1,49)
    if randomNumber not in numbers and len(numbers) < 7:
        numbers.append(randomNumber)
        if len(numbers) == 6:
            numbers.sort()
            print(*numbers)
            key += 1
            numbers = list()

# another example with lists

maList = ["nihil", 24, "programmer", "dreamer"]
key = 0

while key < len(maList):
    for elements in maList:
        print("Index number:", key + 1, "Element:", elements)
        key += 1