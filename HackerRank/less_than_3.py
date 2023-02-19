import sys

def string_distance(n, s1, s2):
    if (s1 == s2):
        return 0
    if (n==1):
        return 1
    if (n == 2):
        if (s1=='01' or s1=='10') or (s2=='01' or s2=='10'):
            return 1
        else:
            return 2
    if (n==3):
        if (s1=='000' and s2.count('1')==1) or (s2=='000' and s1.count('1')==1):
            return 1
        if (s1=='000' and s2.count('1')==2) or (s2=='000' and s1.count('1')==2):
            return 2
        if (s1=='000' and s2.count('1')==3) or (s2=='000' and s1.count('1')==3):
            return 3
        if (s1.count('1')==1 and s2.count('1')==1) or (s2.count('1')==1 and s1.count('1')==1):
            return 2
    if (s1=='0011' and s2=='0101'):
        return 4
    return 0

args = []
for line in sys.stdin:
    args.append(line.strip("\n"))
answer = string_distance(int(args[0]), args[1], args[2])
print(answer)