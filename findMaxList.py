def max_subarray_sum(nums):

    def divide_and_conquer(left, right):
        # 基本情况：只有一个元素
        if left == right:
            return nums[left]

        # 计算中间点,向下取整
        mid = (left + right) // 2

        # 递归计算左半部分和右半部分的最大子数组和
        left_max = divide_and_conquer(left, mid)
        right_max = divide_and_conquer(mid + 1, right)


        # 从中点向左扩展
        left_sum = float('-inf') # 负无穷大的意思，设成最小
        curr_sum = 0
        for i in range(mid, left - 1, -1): # range():包含左不包含右
            curr_sum += nums[i] # 从中间往左走累加
            left_sum = max(left_sum, curr_sum) # 记录遇到的最大值

        # 从中点向右扩展
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)

        # 跨越中间点的最大和
        cross_max = left_sum + right_sum

        # 返回三者中的最大值
        return max(left_max, right_max, cross_max)

    # 一直递归计算“跨越中点的最大值”，最大数组在这些最大值里面
    return divide_and_conquer(0, len(nums) - 1)


n = int(input().strip())
nums = list(map(int, input().strip().split()))

result = max_subarray_sum(nums)

print(result)


