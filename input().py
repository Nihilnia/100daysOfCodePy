# If we want to get some informations from user, we're using input() Function

#How input() Works? Simple and magical asf.

userNick = input("Write your Nick: ")
print("Your nick is:", userNick)
# let's say user wrote 'nihil', our output is like:
# Your nick is: nihil

# DO NOT FORGET: everything is coming as string with input()
#SO! If you wanna make some calculations etc. you should convert types.
#Example:

firstNumber = input("First number: ")
secondNumber = input("Second number: ")

#convert them to integer.
firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

#write to screen
print("First number + Second Number =", firstNumber + secondNumber)

#OR, as you know we can conver them directly.
#Look:

firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))
print("First number + Second Number =", firstNumber + secondNumber)
#Got ya? It's up to you. If you wanna use them always as integers, convert them directly.


#EXERCISES! 

name = input("Name: ")
surName = input("Surname: ")
age = int(input("Old: "))

#Save that infos to a tuple, list and Dictionary.

userInfosTuple = (name, surName, age)
userInfosList = [name, surName, age]
userInfosDict = {"name": name, "surname": surName, "age": age}

#Write that infos at the screen:

#Using tuple:
print("Your name: {}\nYour surname: {}\nAnd your age: {}"
.format(userInfosTuple[0], userInfosTuple[1], userInfosTuple[2]))

#Using List:
print("Your name: {}\nYour surname: {}\nAnd your age: {}"
.format(userInfosTuple[0], userInfosTuple[1], userInfosTuple[2]))

#Using Dictionary:
print("Your name: {}\nYour surname: {}\nAnd your age: {}"
.format(userInfosDict["name"], userInfosDict["surname"], userInfosDict["age"]))



a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = (b ** 2 - 4 * a * c)

birinciKok = (-b - delta ** 0.5) / (2 * a)
ikinciKok = (-b + delta ** 0.5) / (2 * a)

print("Girmiş olduğunuz değerlere göre\nBirinci kök: {}\nİkinci kök: {}"
.format(birinciKok, ikinciKok))