print("\n\n")
print(" "*19,"*")

key = 18
for f in range(3,21,2):
    print(" "*key, "*"*f)
    key -= 1
key2 = 9
for x in range(21,1,-2):
    print(" "*key2, "*"*x)
    key2 += 1

print(" "*19,"*")