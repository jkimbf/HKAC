temp = list(range(2, 1001))
primes = []

while len(temp) != 0:
    cur = temp[0]
    primes.append(cur)
    temp.remove(cur)
    to_remove = list(range(1, (1000//cur)+1))
    to_remove = [x*cur for x in to_remove]

    mask = [x in temp for x in to_remove]

    removed = []
    for i, m in enumerate(mask):
        if m: removed.append(to_remove[i])
        else: continue

    for r in removed:
        temp.remove(r)
input()
inputs = [int(x) for x in input().split()]
print(sum([1 if i in primes else 0 for i in inputs]))
