import sys

def b_together(n, numbers):
    cost = 0
    minimum = float("inf")
    
    if len(set(numbers)) == 1:
        return cost
    for i in range(min(numbers), max(numbers)):
        total = sum([(x-i)**2 for x in numbers])
        if total < minimum:
            minimum = total
    return minimum

args = []
for line in sys.stdin:
    args.append(line.strip('\n'))
    
numbers = [eval(i) for i in args[1].split(' ')]
minimum = b_together(int(args[0]), numbers)
print(minimum)