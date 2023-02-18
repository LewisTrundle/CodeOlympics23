import sys

def find_index(problemID):
    problemID = str(problemID)
    pIndex = 0
    for character in problemID:
        currentDigit = (ord(character) - ord('A') + 1)
        pIndex = pIndex * 26 + currentDigit
    print(pIndex)
    return pIndex

for line in sys.stdin:
    line = line.strip()
    find_index(line)
