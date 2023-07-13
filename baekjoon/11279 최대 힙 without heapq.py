import sys

class max_heap():
    def __init__(self) -> None:
        self.heap = [0]
        self.capacity = 0
    def push(self, N):
        if len(self.heap) - 1 == self.capacity:
            self.heap = self.heap + [0] * len(self.heap)
        self.capacity += 1
        self.heap[self.capacity] = N
        temp_num = self.capacity
        while temp_num > 1:
            if self.heap[temp_num] > self.heap[temp_num//2]:
                temp = self.heap[temp_num]
                self.heap[temp_num] = self.heap[temp_num//2]
                self.heap[temp_num//2] = temp
                del temp
                temp_num //= 2
            else:
                break
        del temp_num
    def pop(self) -> int:
        if self.capacity == 0:
            return 0
        p = self.heap[1]
        self.heap[1] = self.heap[self.capacity]
        self.heap[self.capacity] = 0
        temp_num = 1
        while(self.capacity > temp_num * 2):
            if self.heap[temp_num * 2] == 0 and self.heap[temp_num * 2 + 1] == 0:
                break
            if self.heap[temp_num] < max(self.heap[temp_num * 2], self.heap[temp_num * 2 + 1]):
                temp = self.heap[temp_num]
                if self.heap[temp_num * 2] > self.heap[temp_num * 2 + 1]:
                    self.heap[temp_num] = self.heap[temp_num * 2]
                    self.heap[temp_num * 2] = temp
                    temp_num *= 2
                else:
                    self.heap[temp_num] = self.heap[temp_num * 2 + 1]
                    self.heap[temp_num * 2 + 1] = temp
                    temp_num = temp_num * 2 + 1
            else:
                break
        self.capacity -= 1
        return p

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    heap = max_heap()
    for i in range(N):
        integer = int(sys.stdin.readline())
        if integer:
            heap.push(integer)
        else:
            print(heap.pop())