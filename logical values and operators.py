#boolean values
#True and False

a = True
print(type(a))
# <class 'bool'>

b = False
print(type(b))
# <class 'bool'>

# If a number is not zero, it's always True

print(bool(0.1))
#True

print(bool(12))
#True

print(bool(0))
#False

print(bool(0.0000000000000001))
#True


# None
#if you do not want to give any value to variable, you can give None

a = None
print(bool(a))
#False

#and you can give any value to that variable anytime
a = "nihil"
print(a, bool(a))
#nihil True


# Comparison Operators

x = 1
y = 2

print(x > y) #False
print(x < y) #True

print(x >= y) #False
print(x <= y) #True

print(x == y) #False
print(x != y) #True

print("Nihil" == "nihil") #False
print("Nihil" != "nihil") #True
