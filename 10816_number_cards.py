from sys import stdin
A, T = [l.split() for l in stdin.read().splitlines()[1::2]]
d = dict.fromkeys(set(A), )
print(*[1 if t in A else 0 for t in T], sep='\n')