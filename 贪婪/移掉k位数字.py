'''
s, k = input().split()
arr = list(map(int, s))
k = int(k)

arr1 = arr
arr.sort(reverse = True)
arr2 = [0] * k

for i in range(k + 1):
    arr2[i] = arr[i]

flag = 0
for i in range(len(arr1)):
'''