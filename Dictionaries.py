#Dictionaries
# dictName = {key:value, key: value, key:value}
#or
# dictName = dict()
#or
# dictName = {}


exampDict = {"a":1, "nihil":0.1, 3.14:"pi"}
print(exampDict[3.14])
#pi

print(exampDict["nihil"])
#0.1

exampDict2 = {"list1":["abc",12], "list2":[[1234, 32423], ["nihil", 24]]}
#if we want to reach "nihil" from that dict
print(exampDict2["list2"][1][0])

#Dictionaries  has no index numbers like lists and tuples.
#So, sequence is not important. That's good.

#When we add new key to dictionaries, that new key would be last key in the dictionary.
#example:

exampDict2["jobs"] = "mac"
print(exampDict2)
#{'list1': ['abc', 12], 'list2': [[1234, 32423], ['nihil', 24]], 'jobs': 'mac'}

exampDict2["gates"] = "pc"
print(exampDict2)
#{'list1': ['abc', 12], 'list2': [[1234, 32423], ['nihil', 24]], 'jobs': 'mac', 'gates': 'pc'}


#how to change a key from the dictionary?
#Same like add a new key. Watch:
exampDict3 = {"a": 1, "b": 2, "c": 3}
print(exampDict3["c"])
#3

#lets make c = 4
exampDict3["c"] = 4
print(exampDict3["c"])
#4

#lets make it 5
exampDict3["c"] += 1
print(exampDict3["c"])
#5


#what if a dictionary has few dictionary?
#Would be more cooler right? 
adDict = {"adDict1": {"abc": 1, "edf": 2}, "addict2": {"log": bool, "gem": "crystal"}}
#lets reach gem's value
print(adDict["addict2"]["gem"])


#SOME FUNCTIONS OF DICTIONARIES 

#keys() - Python give you keys as list from your dictionary.
nihil = {"a":1, "b": 2}
print(nihil.keys())
#dict_keys(['a', 'b'])

#values() - Python give you values as list from your dictionary.
print(nihil.values())
#dict_values([1, 2])

#items() - Python give you keys and values as tuples in a list from your dictionary. (My english suck.)
print(nihil.items())
#dict_items([('a', 1), ('b', '2')])


# An example with For loop
for keys, values in nihil.items():
    print("""
"key" {}'s value = {}""".format(keys, values))
    
