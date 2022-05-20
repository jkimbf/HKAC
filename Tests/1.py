def solution2(A):
    # O(N)
    count_neg = 0
    for a in A:
        if a < 0:
            count_neg += 1
        elif a == 0:
            return 0
    return -1 if count_neg % 2 == 1 else 1

def solution(A):
    if 0 in set(A):
        return 0
    else:
        A = list(filter((0).__ge__, A))
        return -1 if len(A) % 2 == 1 else 1

print(solution([1,2,3,1234,63,2,-1,2,-3,-2]))
print(solution([-1,-1000,-2,0]))
print(solution([-1,-1000,-2,-0]))
print(solution([0]))