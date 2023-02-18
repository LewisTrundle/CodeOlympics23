import sys

def distribute(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
    
for line in sys.stdin:
    distribute(int(line))