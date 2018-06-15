# Factorial

while True:
    userNumber = int(input("Give me a number and i tell you factorial of that number: "))
    if type(userNumber) == type(12):
        if userNumber != 1 and userNumber != 0:
            userFactorial = 1
            for f in range(userNumber, userNumber - userNumber, -1):
                userFactorial *= int(f)
            print(userNumber, "factorial =", userFactorial)
        else:
            print(userNumber, "factorial = 1")
    else:
        print("I Said a number..")
    
# OR

while True:
    userNumber = input("Sayi giriniz: ")
    if userNumber == "q":
        print("Programdan cıkılıyor..")
        break
    userNumber = int(userNumber)
    factorial = 1
    for f in range(2, userNumber + 1):
        factorial *= f
        print("{} factorial = {}".format(f, factorial))
    print(factorial)