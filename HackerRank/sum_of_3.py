import sys

def sumOf3(k, s):
    total = 0
    for x in range(k+1):
        for y in range(k+1):
            z = s - (x + y)     # calculate potential z value given x and y
            if 0 <= z <= k:
                total += 1
    print(total)


for line in sys.stdin:
    k, s = line.split(' ')
    sumOf3(int(k), int(s))