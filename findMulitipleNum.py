def choose(nums):
    count = 0
    can = 0
    for num in nums:
        if count == 0:
            can = num
        if num == can:
            count += 1
        else:
            count -= 1
    return can


n = int(input())                    # 读取数组长度
nums = list(map(int, input().split()))  # 读取数组元素
print(choose(nums))