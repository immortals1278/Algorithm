s = input()

arr = list(map(int, input().split()))
num = 1
maxSum = 0
for i in arr:
    sum = i
    if sum > maxSum:
        maxSum = sum
    for j in range(num,len(arr)):
        sum += arr[j]
        if sum > maxSum:
            maxSum = sum
    num += 1
print(maxSum)