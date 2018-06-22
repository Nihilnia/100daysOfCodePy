# return gives us values. Without return we wouldn't get any value
# let's make it clear with an example:

#without return

def addition(firstNumber, secondNumber):
    print(firstNumber + secondNumber)

addition(2, 3)

# we can write the result on the screen but we cant transfer that result to any variable
# example

result = addition(2, 3)
print(result) # if you run this codes, you will get an error.

# We can't transfer of the addition funtion's result to any variable, bc we don't have any return.

#Let's make it with return

def addition(firstNumber, secondNumber):
    return firstNumber + secondNumber

result = addition(2, 3)
print(result)
# as you can see we did transfer succesfuly.
# and we wrote the result on the screen.


# another example

def division():
    firstNumber = int(input("Give me the first number: "))
    secondNumber = int(input("Give me the second number: "))
    return firstNumber / secondNumber

result = division()
print(result)

# and another example of course:

def firstFunction(a):
    print("First function worked, and result:", a + 2)
    return a + 2

def secondFunction(a):
    print("Second function worked, and result:", a * 3)
    return a * 3

def thirdFunction(a):
    print("Third function worked, and result:", a ** 2)
    return a ** 2

print(thirdFunction(secondFunction(firstFunction(2))))
# that's mean actually this : print(thirdFunction(12))
# so, final result 12 ** 2


# NOTE!!!

# after return codes doesnt work. return is end for a function.
# for example if you want to write somethings on the screen, you should code that before your return.

# example:


def xyz(x, y , z):
    return x + y - z 
    print("This is a function!")
    

print(xyz(1,2, 3))

# if we do like that, our print function won't work.

# do it like that, nc return is end for the function

def xyz(x, y , z):
    print("This is a function!")
    return x + y - z 

print(xyz(1,2, 3))