while True:
    nums = sorted(map(int, input().split()))
    if not all(nums): break
    print("right") if nums[2]**2 == sum([n**2 for n in nums[:2]]) else print("wrong")