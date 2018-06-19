# armstrong Number questioning

import math

while True:
    number = input("Give me a number: ")
    exponential = len(number)
    total = 0
    for fuck in number:
        fuck = int(fuck)
        total += pow(fuck, exponential)
        print("Number:", number, "Total:", total)
    if total == int(number):
        print("It's an armstrong number.")
    else:
        print("It isn't an armstrong number.")
