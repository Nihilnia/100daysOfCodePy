# parameters In Functions

# we dont have to give parameters to a function everytime.
# Look at that:

def hello(nick):
    print("hello", nick)

#if we want to use that Function, we have to give a parameter.
#like that:

hello("nihil")
hello("okan")

# if we don't want to give a parameter when we're using a Function,
# we can make a default parameter.

def hello(nick = "nihil"):
    print("hello", nick)

hello()

#got ya?

#another example:

def student(name, surname, number):
    print("Name: {} Surname: {} and Number: {}".format(name, surname, number))

student("okan", "topal", 2771)

# and

def student(name = "okan", surname = "topal", number = 2771):
    print("Name: {} Surname: {} and Number: {}".format(name, surname, number))

student()

# as you can see we can define default values of parameters.

# lets say, our Function have 3 parameter, and we define them as default, but we are insert 2 parameter when using.
# there is no problem with day, watch it!:

def student(name = "unknown", surname = "unknown", number = 0000):
    print("Name: {} Surname: {} and Number: {}".format(name, surname, number))

student("okan", "topal")

# gotYa?

# but a problem here: Let's say user just give student's number parameter?
# i mean like that:

student(2771) #our first parameter is name, but we gavee us number as first parameter.

# this is a problem. But solution is not so complicated. When we are using a Function like that,
# we should make specify. Watch it:

student(number = 2771) #got ya?

# SIMPLE! 

#Let's create a print function.

def writeOnScren(value1 = "", value2 = "", value3 = "", value4 = "", value5 = "", value6 = "", seperate = " "):
    for f in value1, value2, value3, value4, value5, value6:
        print(f + seperate, end ="")

writeOnScren("okan", "topal")


# flexible parameters.
# as you know, when we define a function, we are define some parameters.
# and when we are using that Function, we are giving parameters.
# But what if we are using much more parameter than defined.

# I mean:

def thisIsAFunction(a, b, c):
    print(a + b + c)

thisIsAFunction(1, 2, 3, 4, 5, 6)

#we define 3 parameters but we gave 6 parameters?
# for this we can make somethings like that:

def thisIsAFunction(*a):
    print(a)

thisIsAFunction(1, 2, 3, 4, 5, 6)

# what if we want to make addition (my english best.)

def thisIsAFunction(*a):
    total = 0
    for numbers in a:
        total += numbers
    print(total)

thisIsAFunction(1, 3, 5)


# lets make a print funtion again with flexible parameter.

def writeIt(*thisWillBeWrited):
    writeThem = []
    for values in thisWillBeWrited:
        writeThem.append(values)
    print(*writeThem)

writeIt("okan", "topal", "nihil", 24)