import sys

def djkistra(n, m, edges):
    return 0
    

args = []
for line in sys.stdin:
    args.append(line.strip("\n"))

n, m = args[0].split(" ")
edges = [x.split(" ") for x in args[1:]]
answer = djkistra(int(n), int(m), edges)
print(answer)