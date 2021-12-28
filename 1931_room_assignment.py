from sys import stdin
nums = [(int(l.split()[0]), int(l.split()[1])) for l in stdin.read().splitlines()[1:]]
nums = sorted(nums, key=lambda x: (x[1], x[0]))

count = 1
last = nums[0][1]
for n in nums[1:]:
    if n[0] >= last:
        count += 1
        last = n[1]

print(count)