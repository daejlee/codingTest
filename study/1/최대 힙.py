from sys import stdin
import heapq

heap = []
n = int(stdin.readline())
GET_MAX = 0
for _ in range(n):
    op = int(stdin.readline())
    if op == GET_MAX:
        if len(heap) == 0:
            print(0)
            continue
        print(-(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -op)
