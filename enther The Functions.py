def yo():
    print("Ayy!")

yo()

def name(name):
    print("Hello", name)

name("nihil")

def age():
    age = input("Your age: ")
    print(age)

age()


# with parameters and arguments

def heyya(name):
    print(name)

heyya("nihil") # we had to give an argument, bc our function have a parameter


# let' define a function for addition operation (my english best!)

def addition(a, b):
    a = int(a)
    b = int(b)
    print("{} + {} = {}".format(a, b, a + b))

addition(2, 3)

# let's create a function for factorial calculate!

def factorial(number):
    number = int(input("Give me a number: "))
    total = 1
    if number == 0 or number == 1:
        print("Factorial of",number,"= 1")
    else:
        for f in range(1, number + 1):
            total *= f
        print("Factorial of", number,"=",total)
 
factorial(5)