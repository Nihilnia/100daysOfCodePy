#Exercise - 1:
#Get 3 number from user. Multiply that number and write result to the screen. Try to use format() function.

number1 = int(input("Please write first number: "))
number2 = int(input("Please write second number: "))
number3 = int(input("Please write third number: "))

result = number1*number2*number3

print("""
Your first number was: {0}
Your second number was: {1}
Your third number was: {2}
{0} x {1} x {2} = {3}\n""".format(number1, number2, number3, (result)))


#Exercise - 2:
#Get weight and height values from user. Calculate height - weight index

userHeight = int(input("Please write your height cm (ex. 180): "))
userWeight = int(input("Please write your weight as kilo (ex. 75): "))

userResult = (userWeight/(userHeight ** 2))

print("""
Your height: {0}
Your weight: {1}
Your result: {2}""".format(userHeight, userWeight, userResult))

#Exercise - 3:
#Take the amount of information that a vehicle has used how many kilometers it has traveled,
#and How much price does user's car spend on a kilometer
#calculate how much of the driver has to pay in total.

carKM = int(input("How many kilometers you did?: "))
gasoline = int(input("How much gasoline does your car spend on a kilometer?: "))

totalPay = carKM * gasoline

print("""
You passed {0}
Your car using ${1} for a kilometer.
So, your total bill: ${2}""".format(carKM, gasoline, totalPay))

#Exercise - 4:
#Get user's name, surname and phone number and write them on the screen. lol

userName = input("What's your name?\n")
userSurname = input("What's your surname?\n")
userPhoneNumber = input("What's your phone number?\n")

print("""
Your name:    {0}
Your surname: {1}
Your phone:   {2}""".format(userName, userSurname, userPhoneNumber))

#Exercise - 5:
#Get two number from user, and change the values each other.

firstNumber = int(input("First number? "))
secondNumber = int(input("Second number? "))

firstNumber, secondNumber = secondNumber, firstNumber
print("""
For exercise, your number's values changed each other.
Your first number was: {1}, but now: {0}
Your second number was: {0}, but now: {1} """.format(firstNumber, secondNumber))

#Exercise - 6:
#Calculate the hypotenuse. 37 53

a = float(input("Please write first length: "))
b = float(input("Please write second length: "))
# hypotenuse^2 = a^2 + b^2
hypotenuse = (a**2 + b**2)**0.5

print(hypotenuse)
