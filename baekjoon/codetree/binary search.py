n, m = map(int, input().split())
arr = list(map(int, input().split()))

def search(Num):
    left, right = 0, n-1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == Num:
            return mid
        elif arr[mid] > Num:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

for _ in range(m):
    x = int(input())
    index = search(x)
    
    print(-1 if index < 0 else index + 1)