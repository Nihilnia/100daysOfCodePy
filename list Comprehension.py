# list Comprehension

myList = [1, 2, 3, 4, 5]
myList2 = list()

for f in myList:
    myList2.append(f)

print("first list:", *myList)
print("second list:", *myList2)

# we know this ay but actually we have more shorter way, look carefuly

exList = [1, 2, 3 , 4, 5]
exList2 = [i for i in exList]
print("exList2:",exList2)

# another example:

deList = [6, 7, 8, 9]
deList2 = [f *3 for f in deList]
print(deList2)

# and the another

xList = [(1, 2), (3, 4), (5, 6)]
xList2 = [f * k for f, k in xList]
print(xList2) #[2, 12, 30]

# an example with a string

gg = "coding"
ggList = [f * 3 for f in gg]
print(*ggList)

# lists in list

xList = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
yList = [a for b in xList for a in b]
print(yList)


# another example

restless = [[24, "nihil"], ["spotify"], ["gitHub", 123]]
rollup = [newItems for oldItems in restless for newItems in oldItems]
print(rollup)

for items in rollup:
    if type(items) == type(" "):
        print(items)

# and the another one

listem = [["nihil", 24], ["spotify"], [123, "abc"]]
yeniListem = [yeniOgeler for eskiOgeler in listem for yeniOgeler in eskiOgeler]
for xyz in yeniListem:
    if type(xyz) == type("abccdsasedwa"):
        print(xyz)