MAX = 200000

N = int(input())
arr = [
    tuple(map(int, input().split())) for _ in range(N)
]

checked = [0] * (MAX + 1)
ans = 0

for x1, x2 in arr:
    checked[x1] += 1
    checked[x2] -= 1


overlapped_cnt = 0
for x in range(1, MAX+1):
    overlapped_cnt += checked[x]
    ans = max(ans, overlapped_cnt)

print(ans)