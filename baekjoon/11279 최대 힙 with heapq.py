from heapq import heapify, heappop, heappush
import sys

if __name__ == "__main__":
    heap = []
    heapify(heap)
    N = int(sys.stdin.readline())
    for i in range(N):
        tmp_int = int(sys.stdin.readline())
        if tmp_int == 0:
            try:
                print(-1 * heappop(heap))
            except IndexError:
                print(0)
        else:
            heappush(heap, -1 * tmp_int)