from collections import deque
N, K = map(int, input().split())
diff = abs(N-K)
queue = deque([(N, 0)]) # append and popleft
check = [False]*100001

if K <= N:
    print(diff)
else:
    while queue:
        cur, count = queue.popleft()
        if count > diff or cur > K*2 or cur < 0 or cur > 100000 or check[cur]:
            continue
        check[cur] = True
        if cur != K:
            queue.append((2*cur, count+1))
            queue.append((cur+1, count+1))
            queue.append((cur-1, count+1))
        else:
            print(count)
            break