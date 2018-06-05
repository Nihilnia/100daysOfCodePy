# if (condition):
#   processes

a = 0
if a == 0:
    print("a is 0")

# elif (condition):
#   processes

# elif block works if previous if condition turn false.

a = 0
if a == 0:
    print("a is 0")
elif a > 0:
    print("a > 0")

# else:
# if previous condition turn false, else works.

a = 0
if a == 0:
    print("a is 0")
elif a > 0:
    print("a > 0")
else:
    print("a < 0")