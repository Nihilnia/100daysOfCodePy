print("""
Welcome to "VERY" Basic Calculator.
Please let me know what do you want!""")

while True:
    operation = input("+ - / or *: ")
    if operation in "+/-*" and operation:
        firstNumber = float(input("Please write first number: "))
        secondNumber = float(input("Please write second number: "))
        if operation == "+":
            print("{} + {} = {}".format(firstNumber, secondNumber, firstNumber+secondNumber))
        elif operation == "-":
            print("{} - {} = {}".format(firstNumber, secondNumber, firstNumber-secondNumber))
        elif operation == "/":
            print("{} / {} = {}".format(firstNumber, secondNumber, firstNumber/secondNumber))
        else:
            print("{} x {} = {}".format(firstNumber, secondNumber, firstNumber*secondNumber))
    else:
        print("Please write only + - / or *")