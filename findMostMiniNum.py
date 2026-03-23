def find(nums,k):
    nums.sort(reverse = True)
    for i in nums:
        k -= 1
        if k == 0:
            return i


a, b = map(int, input().split())             # 一次读取两个值
nums = list(map(int, input().split()))
print(find(nums,b))
