import sys
from fractions import Fraction
from decimal import Decimal

def stingy(userInput):
    a,b,c,x = [int(i) for i in userInput.split(' ')]
    if (a < 1 or a >= b or b > 1000 
    or c < 1 or c > (b-a)
    or x < 1 or x > 1000):
        return
    if (x <= a):
        print(1.0)
        return 1.0
    elif (x<=b):
        prob = c / (b-a)
        print(prob)
        return prob
    else:
        print(0.0)
        return 0.0

for line in sys.stdin:
    stingy(line)