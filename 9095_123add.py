from sys import stdin
lines = stdin.read().splitlines()
nums = [1, 2, 4, 7]+[0]*7
for i in range(4, 11):
    nums[i] = sum(nums[i-3:i])
print(*[nums[int(x)-1] for x in lines[1:]], sep='\n')