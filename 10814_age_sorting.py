from sys import stdin
print(*sorted(stdin.read().splitlines()[1:], key=lambda x: int(x.split()[0])), sep='\n')