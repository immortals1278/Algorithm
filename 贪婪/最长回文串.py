s1 = input()

d = {}
num = 0

for key in s1:
    if key not in d:
        d[key] = 1
    if d.get(key) == 2:
        del d[key]
        num += 2
    if d.get(key) == 1:
        d[key] += 1

if num * 2 != len(s1):
    num += 1
print(num)