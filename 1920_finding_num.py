from sys import stdin
A, T = [l.split() for l in stdin.read().splitlines()[1::2]]
A = set(A)  # lowering time complexity
print(*[1 if t in A else 0 for t in T], sep='\n')