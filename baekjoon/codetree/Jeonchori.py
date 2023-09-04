string = input()
n = len(string)
R = [0] * n

R[n - 1] = 0
for i in range(n-2, -1, -1):
    if string[i] == ')' and string[i + 1] == ')':
        R[i] = R[i + 1] + 1
    else:
        R[i] = R[i + 1]
ans = 0
for i in range(n - 2):
    if string[i] == '(' and string[i + 1] == '(':
        ans += R[i + 2]

print(ans)