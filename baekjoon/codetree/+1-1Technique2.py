N = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

points = dict()
for a, b in segments:
    try:
        points[a] += 1
    except:
        points[a] = 1
    try:
        points[b] -= 1
    except:
        points[b] = -1

ans = 0

key = list(points.keys())
key.sort()
search = 0

for i in key:
    search += points[i]
    if search == 0:
        ans += 1
print(ans)