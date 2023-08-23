import sys

INT_MIN = -sys.maxsize

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
ans = INT_MIN

prefix_sum[0] = 0
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for i in range(1, n - k + 2):
    ans = max(ans, prefix_sum[i + k - 1] - prefix_sum[s - 1])

print(ans)