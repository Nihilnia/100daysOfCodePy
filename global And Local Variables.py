# global And Local Variables

# two kind of variable type's with us (My english always best!)

#  Global & Local Variables
#But.. What does it mean?

# Shortly..
#Global variables can use everywhere.
#Local variables can use for a function block or class.

#Look at this example:

xayah = 10 # it's a GLOBAL Variable

def rakan():
    xayah = 20 # it's a LOCAL Variable, this change doesn't effect our Local variable.
    return xayah
    

print("Local Xayah' s value:", rakan())
print("Global Xayah' s value:", xayah)
print("Local:",rakan(), "+", "Global:", xayah, "=", rakan() + xayah)

# as you can see the value of the Global variable still the same. Even we did a change in function.
#It's so clear and simple, right?


#But.. What's going on this thing in if-else blocks.

a = 1
while a < 10:
    if a < 5:
        var = a
        print(var)
    else:
        char = var * 2
    a += 1
print("Var:", var, "Char:", char)

# As you can see, a variable is global if defined in a if, else block.

#another example

qlobal = 0
if True:
    qlobal = 1

print(qlobal) #Changes succesful.

#But if we try to change a Global variable in a function' s block.

qlobalx2 = 0
def khan():
    qlobalx2 = 1
    return qlobalx2

print("It's our Global variable:", qlobalx2)
print("It's our changed Global variable:", khan())
print("As you can see our Global variable still the same:", qlobalx2)