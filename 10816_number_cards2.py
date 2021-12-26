from sys import stdin
N, M = [x.split() for x in stdin.read().splitlines()[1::2]]
N_dict = dict.fromkeys(N, 0)
for n in N:
    if n not in N_dict.keys(): continue
    N_dict[n] += 1
print(*[N_dict[m] if m in N_dict.keys() else 0 for m in M], sep=' ')