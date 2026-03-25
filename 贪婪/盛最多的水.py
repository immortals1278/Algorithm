s = list(map(int,input().split()))

Sum = 0
i = 0
j = len(s) - 1

while i != j:
    Sum = max(Sum, min(s[i],s[j]) * (j - i))
    if s[i] < s[j] :
        i += 1
    else:
        j -= 1
print(Sum)


