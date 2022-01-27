from sys import stdin

lines = stdin.read().splitlines()[1:]
for i in range(len(lines)):
    lines[i] = list(map(int, lines[i].split()))

for i in range(1, len(lines)):
    for j in range(3):
        lines[i][j] += min(lines[i-1][j-1], lines[i-1][j-2])

print(min(lines[-1]))