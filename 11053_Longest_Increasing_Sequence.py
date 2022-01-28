from sys import stdin

nums = list(map(int, stdin.readlines()[1].split()))
out = [nums[0]]

for num in nums[1:]:
    found = False
    for i, o in enumerate(out):
        if num <= o:
            out[i] = num
            found = True
            break
    
    if not found:
        out.append(num)

print(len(out))