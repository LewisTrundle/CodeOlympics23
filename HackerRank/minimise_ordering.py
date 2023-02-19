import sys

def minimise_ordering(s):
    print("".join(sorted(s)).strip())

minimise_ordering("bababdsf")
for line in sys.stdin:
    minimise_ordering(line)