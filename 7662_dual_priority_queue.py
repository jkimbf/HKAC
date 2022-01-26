# import sys
# from heapq import heapify, heappush, heappop
# input = sys.stdin.readline

# import time
# time.sleep(2)

# for _ in range(int(input())):
#     max_h = []
#     min_h = []
#     heapify(max_h)
#     heapify(min_h)
#     is_popped = {}
#     heap = [max_h, min_h]

#     for _ in range(int(input())):
#         cmd, num = input().split()
#         num = int(num)
#         if cmd == 'I':
#             heappush(heap[0], -num)
#             heappush(heap[1], num)
#             if num in is_popped.keys():
#                 is_popped[num] += 1
#             else:
#                 is_popped[num] = 1
#         else:
#             h = heap[0] if num == 1 else heap[1]
#             pop_n = -heappop(h) if num == 1 else heappop(h)
#             while is_popped[pop_n] == 0 and h:
#                 pop_n = -heappop(h) if num == 1 else heappop(h)
#             is_popped[pop_n] -= 1
#         # print(is_popped)
#         # print(max_h)
#         # print(min_h)

#     if heap[0] and heap[1]:
#         max_out = -heappop(heap[0])
#         while is_popped[max_out] <= 0 and heap[0]:
#             max_out = -heappop(heap[0])

#         min_out = heappop(heap[1])
#         while is_popped[min_out] <= 0 and heap[1]:
#             min_out = heappop(heap[1])
        
#         if is_popped[max_out] <= 0 or is_popped[min_out] <= 0:
#             print('EMPTY')
#         else:
#             print(max_out, min_out)
#     else:
#         print('EMPTY')

import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

import time
time.sleep(2)

for _ in range(int(input())):
    max_h = []
    min_h = []
    heapify(max_h)
    heapify(min_h)
    is_popped = {}
    heap = [max_h, min_h]

    for _ in range(int(input())):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heappush(heap[0], -num)
            heappush(heap[1], num)
            if num in is_popped.keys():
                is_popped[num] += 1
            else:
                is_popped[num] = 1
        else:
            h = heap[0] if num == 1 else heap[1]
            if h:
                pop_n = -heappop(h) if num == 1 else heappop(h)
                is_popped[pop_n] -= 1

        while heap[0] and is_popped[-heap[0][0]] == 0:
            heappop(heap[0])

        while heap[1] and is_popped[heap[1][0]] == 0:
            heappop(heap[1])

    if heap[0] and heap[1]:
        max_out = -heappop(heap[0])
        while is_popped[max_out] <= 0 and heap[0]:
            max_out = -heappop(heap[0])

        min_out = heappop(heap[1])
        while is_popped[min_out] <= 0 and heap[1]:
            min_out = heappop(heap[1])
        
        if is_popped[max_out] <= 0 or is_popped[min_out] <= 0:
            print('EMPTY')
        else:
            print(max_out, min_out)
    else:
        print('EMPTY')