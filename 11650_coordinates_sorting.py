from sys import stdin
print(*sorted(set(stdin.read().splitlines()[1:]), key=lambda x: (int(x.split()[0]), int(x.split()[1]))), sep='\n')