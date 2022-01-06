from sys import stdin
nums = [list(map(int, r.split())) for r in stdin.read().splitlines()[1:]]

for r in range(len(nums)-1)[::-1]:
    next_r = nums[r+1]
    for i in range(len(nums[r])):
        nums[r][i] += next_r[i] if next_r[i] > next_r[i+1] else next_r[i+1]

print(nums[0][0])