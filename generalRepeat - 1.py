#### String Indexing and Fragmentation ####

#Indexing!
# howTo?
#  string[start:end(not include):jumping Value]


nick = "nihil"
print(nick[3])
#i (second one)


song = "Ghost-Single Edit"
#let's take it 'Ghost'
print(song[0:5])

#let's take it 'Single Edit'
print(song[6:]) #if value of end is empty, that's mean get it all until the end

#let's take it every second character
print(song[::2])
#GotSnl dt

#TIP!
#just don't take it last character:
print(song[0:-1])

#TIP!
#reverse String
print(song[::-1])

#TIP!
#first character:
print(song[0])

#last character
print(song[-1])


#### Variable Type Converting ####


#Converting!
# howTo?
#   str(variable), int(variable)...

#TIP!
# learning Type of A Variable?
#  type(variable)


firstOne = "12"
print(type(firstOne))
#<class 'str'>

#let's convert it
firstOne = int(firstOne)
print(type(firstOne))
#<class 'int'>

#DO NOT FORGET!
# everything is String what is coming from User
# For a succesful convert, type should be okay for convert.
#Example: "12" is a String but okay for convert to Int, bc of this is a Number.




#### Print Function and Formatting ####

# ofc Do not forget sep and end.
# elements of format function can get number.
print("Hello It's {1}, age {0}, and Language {2}".format(24, "Nihil", "Python"))



#### Lists, Tuples and Dicts ####

#### Lists
# howToCreate?
#  listName = [item0, item1, item2...]
#or
# listName = list[]
#or
# listName = ()

exampleList = ["nihil", 24]
print(*exampleList)
# nihil 24

# elementAdding?
#  listname.append(item) - after that new element would go to end of list.
exampleList.append("Python")
print(*exampleList)
# nihil 24 Python

#or

exampleList = exampleList + ["Computer Science"]
print(exampleList)
# ['nihil', 24, 'Python', 'Computer Science']
# as you can see that last element of list is the new element.

#butWhatIf?
exampleList = ["Computer Science"] + exampleList
print(exampleList)
# ['Computer Science', 'nihil', 24, 'Python']

#lookAtThat!
myList = list("nihil")
print(myList)
#['n', 'i', 'h', 'i', 'l']
# be Careful for that.


#TIP!
# as like Strings, lists are can get Fragmentation either.
# let's take it 24 and 'Python from exampleList
takeIt = exampleList[1:]
print(takeIt)

# as A Summary: Methods of Lists
# append() --> item adding
# pop() --> Item deleting
# sort() --> Item alignment

aList = ["chemical"]

#append()
aList.append("brothers")
print(aList)
# ['chemical', 'brothers']

#pop() - If you do not give any parameter to pop(), last item would be delete
aList.pop()
print(aList)
# ['chemical']

# but if
aList = ["chemical", "brothers"]
aList.pop(0)
print(aList)

#sort()
bList = ["b", "a", "c"]
bList.sort()
print(bList)



#### Tuples
# howToCreate?
# tupleName = (element0, element1, element2,...)

# DO NOT FORGET!
#You can't change the tuples.

# functions of Tuples:
#count() - parameter is Element name, if parameter not in the Tuple, python give us 0
#if there is few, Python gives us how much

#example:
aTuple = ("nihil", 24, "24", "nihil")
print(aTuple.count("nihil"))
#2

print(aTuple.count(24))
#1

print(aTuple.count("24"))
#1

print(aTuple.count("Python"))
#0

print(aTuple.count("NIHIL"))
#0
# BUT
print(aTuple.count("NIHIL".lower()))
#2



#index() - Python gives us first index number of parameter (ofc if parameter is in the Tuple)




#### Dictionaries

#howToCreate
# dictName = {"item": value, item: "value",...}

#call
exampleDict = {0: "zero", 1: "one", 2: "two"}
userInput = input("0 - 1 - 2: ")
print(exampleDict[int(userInput)])

#item-value adding

exampleDict[3] = "three"
#When u add an item-value, that new value goes to end of the dict.
#But order is not important bc while call an value, we are not giving index number.
#We're giving item name.

#item-value deleting
del exampleDict[1]
print(exampleDict)

#basic Function of Dictionaries

aeDict = {0: "zero", 1: "one", 2: "two"}

#key()
#Python gives us keys
print(aeDict.keys())
# dict_keys([0, 1, 2])

#value
#Python gives us values of keys
print(aeDict.values())
#dict_values(['zero', 'one', 'two'])

#item()
#Python gives us keys and values
print(aeDict.items())
#dict_items([(0, 'zero'), (1, 'one'), (2, 'two')])


# WHAT IF DICTs IN DICTS?!

yaDict = {"firstDict": {"firstKey": "firstValue", "secondKey": "secondValue"}}
#call second key of first dict
print(yaDict["firstDict"]["secondKey"])
#secondValue