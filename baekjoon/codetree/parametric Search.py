MAX_N = 10e+9

s = int(input())

left = 1
right = MAX_N
max_num = 0

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        left = mid + 1
        max_num = max(max_num, mid)
    else:
        right = mid - 1

print(max_num)