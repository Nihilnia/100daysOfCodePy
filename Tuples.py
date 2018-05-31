# Tuples

# can't modified. Read only!

tupleOne = ("nihil", 24, "passion", 24)

print(tupleOne[2])
#passion

print(*tupleOne[:2])
#nihil, 24

#there is two methods for Tuples, count() and index()

#count()
print(tupleOne.count(24))
#2 - if paramater not exist, Python give you 0

#index()
print(tupleOne.index(24))
#1 - if parameter is not single in Tuple, Python give you first one' s index number.
#    if parameter is not exist, you would get error msg.
print(tupleOne.index("abc"))
#ValueError: tuple.index(x): x not in tuple

#and last example for that subject.
tupleTwo = ("facebook", "twitter")
print("%s and %s suck." %tupleTwo)