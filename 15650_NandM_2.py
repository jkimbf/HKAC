from collections import deque

def backtracking(N_list, seq, start, length):
    if length == 0:
        print(*seq, sep=' ')
        return

    for i, n in enumerate(N_list[start:]):
        seq.append(n)
        backtracking(N_list, seq, i+start+1, length-1)
        seq.pop()

if __name__ == '__main__':
    N, M = map(int, input().split())
    backtracking(list(range(1, N+1)), deque(), 0, M)