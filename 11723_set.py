from sys import stdin

n = 20
S = 0b0

for _ in range(int(stdin.readline())):
    line = stdin.readline().split()
    cmd = line[0]
    if len(line) == 2:
        num = int(line[1])-1

    if cmd == "add" and S & (1 << num) == 0:
        S |= (1 << num)
    elif cmd == "remove" and S & (1 << num) != 0:
        S &= ~(1 << num)
    elif cmd == "check":
        print(1 if S & (1 << num) else 0)
    elif cmd == "toggle":
        S ^= (1 << num)
    elif cmd == "all":
        S = (1 << n) - 1
    elif cmd == "empty":
        S = 0
    
