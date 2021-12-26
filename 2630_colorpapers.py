from sys import stdin

lines = stdin.read().splitlines()[1:]
lines = [x.split() for x in lines]
white, blue = 0, 0

def is_complete(lines):
    global white, blue
    z_count = sum([line.count('0') for line in lines])
    o_count = sum([line.count('1') for line in lines])
    total = z_count + o_count
    if total == z_count:
        white += 1
    elif total == o_count:
        blue += 1
    else:
        is_complete([line[:len(lines)//2] for line in lines[:len(lines)//2]])
        is_complete([line[len(lines)//2:] for line in lines[:len(lines)//2]])
        is_complete([line[:len(lines)//2] for line in lines[len(lines)//2:]])
        is_complete([line[len(lines)//2:] for line in lines[len(lines)//2:]])

is_complete(lines)
print(white)
print(blue)