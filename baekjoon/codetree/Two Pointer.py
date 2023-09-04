n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = n + 1
sum_val = 0
j = 0
for i in range(n):
    while j + 1 <= n and sum_val < s:
        sum_val += arr[j]
        j += 1
    if sum_val < s:
        break
    ans = min(ans, j - i)
    sum_val -= arr[i]

if ans == n+1:
    ans = -1
print(ans)