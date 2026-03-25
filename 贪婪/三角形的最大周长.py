s = list(map(int,input().split()))

s.sort(reverse = True)

def func(s):
    for i in range(len(s)):
        for j in range(i + 1,len(s)):
            for k in range(j + 1,len(s)):
                if s[i] + s[j] > s[k] and s[i] - s[j] < s[k]:
                    return s[i] + s[j] + s[k]
    return 0
print(func(s))