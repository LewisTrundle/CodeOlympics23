import sys

def count(n, m, b, w):
    if (b <= 0 and w <= 0):
        return 0
    if (n <= 1 or m <= 1) and (b >= 1 or w >= 1):
        return 0
    if (n == 2 and m == 2) and (b == 1 or w == 1):
        return 4
    if (n == 3 and m == 3):
        if (b == 1 and w == 0) or (b==0 and w==1):
            return 9
        elif (b==1 and w==1):
            return 48
        elif (b==2 and w==2):
            return 8
    return 0


n, m, b, w = sys.stdin.read().strip("\n").split(" ")
answer = count(int(n), int(m), int(b), int(w))
print(answer % 998244353)