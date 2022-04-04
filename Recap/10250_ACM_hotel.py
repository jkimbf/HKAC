from sys import stdin
lines = stdin.readlines()[1:]

for line in lines:
    H, W, N = map(int, line.split())
    floor, num = (N%H, N//H + 1) if N % H != 0 else (H, N//H)
    print("{}{:02}".format(floor, num))

# 17
# 1 1 1
# 99 99 9800
# 10 10 99
# 2 2 4
# 3 70 144
# 6 12 12
# 6 12 10
# 6 12 72
# 30 50 72
# 2 10 2
# 2 10 4
# 2 10 20
# 1 99 21
# 2 1 2
# 1 11 11
# 10 10 1
# 2 82 18

# //101
# //9899
# //910
# //202
# //348
# //602
# //402
# //612
# //1203
# //201
# //202
# //210
# //121
# //201
# //111
# //101
# //209