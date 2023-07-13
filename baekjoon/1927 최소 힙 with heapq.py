import sys
import heapq

if __name__ == "__main__":
    numbers = int(sys.stdin.readline())
    heap = []
    for _ in range(numbers):
        num = int(sys.stdin.readline())
        if num != 0:
            heapq.heappush(heap, num)
        else:
            try:
                print(heapq.heappop(heap))
            except:
                print(0)