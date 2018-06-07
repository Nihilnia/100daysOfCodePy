# Exercise - 1:
# Get user's weight and height values, calculate body index and if:

# BKİ 18.5'un altındaysa -------> Weak

# Index 18.5 between 25 ------> Normal

# Index 25 between  30 arasındaysa --------> overweight

# Index above 30 ------------> Obese

# Index calculate: Weight / Height(m) *  Height(m)

userWeight = float(input("Please write your current weight: "))
userHeight = float(input("Please write your current height: "))

bodyIndex = userWeight / (userHeight * userHeight)
print("\nYour body index = ",bodyIndex)

if bodyIndex < 18.5:
    print("You're weak.")
elif bodyIndex >= 18.5 and bodyIndex < 25:
    print("Normal")
elif bodyIndex >= 25 and bodyIndex <= 30:
    print("Overweight!")
else:
    print("Obese!")


# Exercise - 2:
# Get three number from user, and write biggest number to the screen. WHAT A EXERCISE!

firstNumber = int(input("Please write a number: "))
secondNumber = int(input("Please write a number: "))
thirdNumber = int(input("Please write a number: "))

allNumbers = [firstNumber, secondNumber, thirdNumber]
allNumbers.sort()


print(allNumbers[0])

#or 

if firstNumber>secondNumber and firstNumber>thirdNumber:
    print("First number",firstNumber,"is the biggest number.")
elif secondNumber>firstNumber and secondNumber>thirdNumber:
    print("Second number",secondNumber,"is the biggest number.")
else:
    print("Third",thirdNumber,"is the biggest number.")


# Exercise - 3:
# Get three exam results from user, and calculate as:

# First exam will be %30 of result.

# Second exam will be %30 of result.

# Final exam will be %40 of result.


    # Toplam Not >=  90 -----> AA

    # Toplam Not >=  85 -----> BA

    # Toplam Not >=  80 -----> BB

    # Toplam Not >=  75 -----> CB

    # Toplam Not >=  70 -----> CC

    # Toplam Not >=  65 -----> DC

    # Toplam Not >=  60 -----> DD

    # Toplam Not >=  55 -----> FD

    # Toplam Not <  55 -----> FF

firstExamResult = float(input("What's your first exam result?: "))
secondExamResult = float(input("What's your second exam result?: "))
finalExamResult = float(input("What's your final exam result?: "))

total = ((firstExamResult*30)/100) + ((secondExamResult*30)/100) + ((finalExamResult*40)/100)

if total >= 90:
    print("Your result is", total,"and it is AA")
elif total >= 85:
    print("Your result is", total,"and it is BA")
elif total >= 80:
    print("Your result is", total,"and it is BB")
elif total >= 75:
    print("Your result is", total,"and it is CB")
elif total >= 70:
    print("Your result is", total,"and it is CC")
elif total >= 65:
    print("Your result is", total,"and it is DC")
elif total >= 60:
    print("Your result is", total,"and it is CC")
elif total >= 55:
    print("Your result is", total,"and it is DD")
else:
    print("Your result is", total,"and it is FF")



# Exercise - 4:
# Ask to user what he want to calculate, "triangle" or "square".
# If answer is triangle, then as him side values and say what kind of triangle is this.
# Same for square.

userWant = input("Triangle or Square?             ")

if userWant.lower() == "triangle":
    firstSideValue = input("Please write first side value and kill my english: ")
    secondSideValue = input("Please write second side value and kill my english: ")
    thirdSideValue = input("Please write third side value and kill my english: ")

    if firstSideValue == secondSideValue == thirdSideValue:
        print("its a equilateral triangle!")

    elif firstSideValue == secondSideValue or firstSideValue == thirdSideValue or secondSideValue == thirdSideValue:
        print("its a isosceles triangle!")
    
    else:
        print("Idk what kind of triangle is this, fuk.")

elif userWant.lower() == "square":
    firstSideValue = input("Please write first side value and kill my english: ")
    secondSideValue = input("Please write second side value and kill my english: ")
    thirdSideValue = input("Please write third side value and kill my english: ")
    fourthSideValue = input("Please write fourth side value and kill my english: ")

    if firstSideValue == secondSideValue == thirdSideValue == fourthSideValue:
        print("It's a square! ")
    
    elif firstSideValue == secondSideValue:
        print("It's a rectangle")

    elif firstSideValue == thirdSideValue:
        print("It's a rectangle")

    elif firstSideValue == fourthSideValue:
        print("It's a rectangle")

    elif secondSideValue == thirdSideValue:
        print("It's a rectangle")
    
    elif secondSideValue == fourthSideValue:
        print("It's a rectangle")

    elif thirdSideValue == fourthSideValue:
        print("It's a rectangle")
    
    else:
        print("Idk WTF is this!?")