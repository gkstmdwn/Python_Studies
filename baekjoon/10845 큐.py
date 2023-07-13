from collections import deque
import sys

queue = deque()
def push(x:int) -> None:
    queue.append(x)
def pop() -> None:
    try:
        print(queue.popleft())
    except IndexError:
        print(-1)
def size() -> None:
    print(len(queue))
def empty() -> None:
    if len(queue) == 0:
        print(1)
    else:
        print(0)
def front() -> None:
    try:
        print(queue[0])
    except IndexError:
        print(-1)
def back() -> None:
    try:
        print(queue[-1])
    except IndexError:
        print(-1)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        command = sys.stdin.readline().split()
        if command[0] == "push":
            push(command[1])
        elif command[0] == "pop":
            pop()
        elif command[0] == "size":
            size()
        elif command[0] == "empty":
            empty()
        elif command[0] == "front":
            front()
        elif command[0] == "back":
            back()