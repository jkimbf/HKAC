from collections import deque

def backtracking(N_list, seq, start, length):
    if length == 0:
        print(*seq, sep=' ')
        return

    for i, n in enumerate(N_list):
        if n in seq:
            continue
        seq.append(n)
        backtracking(N_list, seq, i+1, length-1)
        seq.pop()

if __name__ == '__main__':
    _, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    backtracking(nums, deque(), 0, M)
