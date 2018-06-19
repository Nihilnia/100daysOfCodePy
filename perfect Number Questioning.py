# perfect Number questioning

while True:
    number = int(input("Give me a number: "))
    divisors = list()
    for f in range(1, number):
        if number % f == 0:
            divisors.append(f)
    
    sums = 0
    for fck in divisors:
        sums += fck
    
    if sums == number:
        print("""This number is PERFECT NUMBER!
Because your number is {}, and this number's full divisors {} and their sum {}."""
.format(number, divisors, sums))
    else:
        print("""This number IS NOT perfect number!
Because your number is {}, and this number's full divisors {} and their sum {}."""
.format(number, divisors, sums))