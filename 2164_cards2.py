from collections import deque

nums = deque()
nums.extend(range(1, int(input())+1))
while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())
print(nums.pop())