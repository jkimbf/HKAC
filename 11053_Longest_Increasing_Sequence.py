from sys import stdin

last_row = [-1, -1]
for i, num in enumerate(map(int, stdin.read().splitlines()[1].split())):
    if num > last_row[-1]:
        last_row.append(num)
    elif num < last_row[-1] and num > last_row[-2]:
        last_row[-1] = num
    elif num < last_row[-2] and num > last_row[-3]:
        last_row[-2] = num

print(len(last_row)-2)