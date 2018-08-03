#range() function
for f in range(10):
    print(f)

#another example
print("Second example!\n\n")
for x in range(11):
    if x % 2 == 0:
        print(x)

#backward?
print("And another\n\n")
for y in range(10,0,-1):
    print(y)


#break and continue
# we know both



#### LIST COMPREHENSIONS ####

# with this 'way' we can make effective and shorter processes.
# watch carefully!

listOne = [1, 2, 3, 4, 5]
listTwo = [items for items in listOne]
print(listTwo)
#we know classic way
listClassic = list()
for f in listOne:
    listClassic.append(f)
print("Classic WAY:")
print(listClassic)
#another example:

listThree = [f*2 for f in listOne]
print(listThree)

#and the another example:

yayo = [(1, 2, 3), (3, 4, 5), (5, 6, 7)]
maList = [x * y + z for x, y, z in yayo]
print(maList)
da = [f[0] * f[1] for f in yayo]
print(da)
# or
toxic = [f[0] + f[1] - f[2] for f in yayo]
print(toxic)



# anf oc the another example:

rightDamn = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newList = [a for b in rightDamn for a in b]
print(newList)

# Long Way (Classic One)
exList = [["nihil", 24], ["24", 4353], ["spotify", 1111], [1212, 1213]]
damnNewList = list()

for f in exList:
    for y in f:
        if isinstance(y, str):
            damnNewList.append(y)

print(damnNewList)

# Short Way (List Comprehensions)

exList = [["nihil", 24], ["24", 4353], ["spotify", 1111], [1212, 1213]]
damnNewList = [a for b in exList for a in b if isinstance(a, str)]
print(damnNewList)