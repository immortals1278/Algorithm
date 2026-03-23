# 子序列可以是不连续的；子数组（子字符串）需要是连续的

s1, s2 = input().split()
num = 0
for ch0 in s1:
    for ch1 in s2:
        if ch0 == ch1:
            num += 1

print(num)