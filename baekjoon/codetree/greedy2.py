import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

ans = INT_MIN

tmp = 0

for i in range(n):
    if tmp < 0:
        tmp = arr[i]
    else:
        tmp += arr[i]
    
    ans = max(ans, tmp)

print(ans)