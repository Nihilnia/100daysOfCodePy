# get a number from user until he wanna stop.
#addit the numbers and write total result on the screen. MY ENGLISH BEST...

total = 0
while True:
    number = input("Give me a number (Q for quit.): ")
    if number.upper() == "Q":
        break
    else:
        total += int(number)
print("Total result:", total)