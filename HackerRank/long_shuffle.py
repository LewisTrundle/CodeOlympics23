def shuffle(l, r):
    if l + 1 == r:
        a[l], a[r] = a[r], a[l]
        return
    mid = (l + r) // 2
    shuffle(l, mid)
    shuffle(mid + 1, r)
    for i in range(l, mid + 1):
        j = mid + 1 + (i - l)
        a[i], a[j] = a[j], a[i]

# t = 7
pairs = ["2 1", "2 2", "5 1", "5 2", "5 3", "5 4", "5 5"]

for pair in pairs:
    n, k = [int(i) for i in pair.split(' ')]
    print(n, k)
    a = list(range(1, n + 1))
    shuffle(n, k)
    # print(a[k - 1])
