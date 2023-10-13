import random

def taek(sex, step = 4):
    if step == 1:
        return sex
    elif step == 4:
        ans = []
        ans_before = taek(sex, step=3)
        for i in ans_before:
            for j in sex:
                ans.append(i + j)
        for i in range(len(ans)):
            ans[i] += "진택"
        return ans
    else:
        ans = []
        ans_before = taek(sex, step = step-1)
        for i in ans_before:
            for j in sex:
                ans.append(i + j)
        return ans


sex = input("진택진택김진택>> ")
list_nickname = taek(sex)
print(list_nickname[random.randint(0, len(list_nickname))])