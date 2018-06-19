# write the numbers which one's can divide with 3
# do it until 100, and try to use Continue

for f in range(1, 101):
    if f % 3 != 0:
        continue
    else:
        print(f)