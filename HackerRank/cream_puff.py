import sys
import math

def distribute(n):
    numbers = []
    if n < 1 or n>10**12:
        return 
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            numbers.append(i)
            if i != n // i:
                numbers.append(n // i)
    numbers.sort()
    for n in numbers:
        print(n)
    
for line in sys.stdin:
    distribute(int(line))