def solution(A):
    digit_sum = [sum(map(int, list(str(x)))) for x in A]    # O(scalar * N)

    d = {}
    for i, d_sum in enumerate(digit_sum):   # O(N)
        d[d_sum] = d[d_sum] + [A[i]] if d_sum in d else [A[i]]

    max_out = -1
    for k in d.keys():
        if len(d[k]) < 2: continue

        two_sum = sum(sorted(d[k], reverse=True)[:2])
        if two_sum > max_out:
            max_out = two_sum

    return max_out

print(solution([51, 71, 17, 42]))
print(solution([42, 33, 60]))
print(solution([51, 32, 43]))
