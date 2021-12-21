import numpy as np
N, M = map(int, input().split())
nums = np.array(list(map(int, input().split())), ndmin=2)
nums_sq = (nums.T + nums).reshape(-1, 1)
nums = (nums_sq + nums).flatten()
nums[nums > M] = 0
print(max(sorted(nums)[:-3]))
