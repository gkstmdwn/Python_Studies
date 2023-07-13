import sys

stack = []
def push(x:int) -> None:
    stack.append(x)
def pop() -> None:
    try:
        print(stack.pop())
    except IndexError:
        print(-1)
def size() -> None:
    print(len(stack))
def empty() -> None:
    if len(stack) == 0:
        print(1)
    else:
        print(0)
def top() -> None:
    try:
        print(stack[-1])
    except IndexError:
        print(-1)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        str = sys.stdin.readline().split()
        if str[0] == 'pop':
            pop()
        elif str[0] == 'size':
            size()
        elif str[0] == 'empty':
            empty()
        elif str[0] == 'top':
            top()
        else:
            push(int(str[1]))