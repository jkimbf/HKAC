def solution(A):
    max_A = max(A)
    range_max = list(range(1, max_A+2)) # 1 greater than max
    A = list(filter((0).__le__, A))
    set_A = set(range_max) - set(A)
    if len(set_A) == 0: return 1
    return min(set_A)

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
