l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

l1.sort()
l2.sort()

m = 0
sum = 0

for i in range(len(l1)):
    for j in range(m,len(l2)):
        m += 1
        if l1[i] <= l2[j]:
            sum += 1
            break

print(sum)


