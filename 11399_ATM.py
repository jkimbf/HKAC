from sys import stdin

nums = sorted([int(x) for x in stdin.read().splitlines()[1].split()])

for i in range(1, len(nums)):
    nums[i] += nums[i-1]

print(sum(nums))