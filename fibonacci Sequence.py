#Fibonacci Sequence

# 1,1,2,3,5,8,13,...

# an example with 1 t0 20

fibonacciList = [0, 1]
key = 0
actualResult = 1
print(actualResult)
for f in range(1, 21):
    actualResult = fibonacciList[key] + fibonacciList[key + 1]
    print(actualResult)
    fibonacciList.append(actualResult)
    key += 1


# other short way

x = 1
y = 1
fibonnaciList = [x, y]

for f in range(21):
    x, y = y, x + y
    fibonnaciList.append(y)

print(fibonnaciList)