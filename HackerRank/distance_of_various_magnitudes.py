import sys
import math

def manhattan(vec):
    return sum(vec)

def euclidean(vec):
    return math.sqrt(sum([x**2 for x in vec]))

def chebyshev(vec):
    return max(vec)

def run(N, xs):
    N = int(N)
    if N < 1 or N > 10**5:
        return
    
    vec = [abs(int(x)) for x in xs.split(" ")]
    for x in vec:
        if x < -(10**5) or x > 10**5:
            return
    
    print(manhattan(vec))
    print(euclidean(vec))
    print(chebyshev(vec))

run(2, "2 -1")

lines = [line for line in sys.stdin]
run(lines[0], lines[1])