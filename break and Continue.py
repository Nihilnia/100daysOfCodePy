# break ---

# in some case, we wanna "break" to loops.
#for example

f = 0
while f < 12:
    print(f, ".Loop")
    f += 1
# it's a classic loop and it will work until f = 12, and last number on the screen = 11, right?

#So, let's say we want that if f = 6, we want to stop to loop.

f = 0
while f < 12:
    print(f, ".Loop")
    f += 1
    if f == 6:
        break
#as you can see that when f = 6 is True, our loop is ending and last number on the screen is 5.

# let's make another example with a For Loop

alias = "nihil"
for f in alias:
    if f == "h":
        print("'h' is founded. Loop is ended u m.fucker.")
        break
    print("letter:", f)

# another VERY BASIC Example
# ask to user for input a name, when he press q, stop asking.


while True:
    userName = input("Give me a name: (\"If you wanna stop, press q:\"): ")
    print("Username:",userName)
    if userName.lower() == "q":
        print("bye bitch!")
        break #we used print() Function before break, bc after break our codes doesn't work.



# continue ---

# as shortly: after continue expression our codes doesnt work and loop going to continue. WOW MY ENGLISH!
#for example: 

for f in range(0,11,2):
    if f == 8 or f == 4:
        continue #when f = 8 and 4, dont do anything and continue to loop. So, our number: 8 and 4 wont be on screen.
    print("Number", f)

# another example

fNumber = 0
while fNumber < 10:
    if fNumber %2 == 0:
        fNumber += 1
        continue # our numbers 0,2,4,6,8 wont be on the screen. 1-3-5-7-9 will be there.
    print("Number:", fNumber)
    fNumber += 1

# last 'important' example

# let's say we have some code lines like that:

num = 0

while num < 5:
    if num > 3: #when our num > 3, this code line will be true and infinite loop come.
        #Why? Bc when our num = 4, loop will be continue forever. Why? Bc we didn't change the num
        #before continue expression. Get it?
        print("Number:",num)
        continue
    print("Number:", num)
    num += 1

# so what's the solution?
# Simple! increase to number before continue

while num < 5:
    if num > 3:
        num += 1 #like that
        continue
    print("Number:", num)
    num +=1 #and as you can see we doing same thing here, if number never < 5, loop always working.
    #Bc in that case number would be always same. Wuhuuu i felt Deja'Vu. Fuck, again! dejavu x2
    