s = list(map(int,input().split()))

num = int(input())

zeros = []
flag = s[0]
cnt = 0
for i in range(len(s)):
    if flag == 1:
        if s[i] == 1:
            cnt = 0
        else:
            flag = 0
            cnt = 1
    elif flag == 0:
        if s[i] == 0:
            cnt += 1
        else:
            flag = 1
            zeros.append(cnt)
            cnt = 0
    if i == len(s):
        zeros.append(cnt)
ans = 0
for i in zeros:
    ans += (i-1)//2

print('true') if ans >= num else print('false')