import sys

def uncommon_prefix(n, s):
    for i in range(1, n):
        l = 0
        for j in range(0, n-1):
            if i+j >= n or s[j] == s[j+i]:
                break
            l += 1
        print(l)
    

args = []
for line in sys.stdin:
    args.append(line.strip('\n'))
uncommon_prefix(int(args[0]), args[1])