def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    total_sum = sum(nums)

    # 基本情况判断
    if k == 1:
        return True
    if total_sum % k != 0:
        return False

    target = total_sum // k

    # 从大到小排序，方便剪枝
    nums.sort(reverse=True)

    # 如果最大值大于目标值，直接返回 False
    if nums[0] > target:
        return False

    n = len(nums)
    used = [False] * n

    def backtrack(start: int, current_sum: int, k_remaining: int) -> bool:
        # 所有子集都构造完成
        if k_remaining == 1:
            return True

        # 当前子集构造完成，开始构造下一个子集
        if current_sum == target:
            return backtrack(0, 0, k_remaining - 1)

        for i in range(start, n):
            if not used[i] and current_sum + nums[i] <= target:
                # 剪枝：如果当前数字和前一个数字相同，且前一个数字没有被使用（说明已经失败过），则跳过
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue

                used[i] = True
                if backtrack(i + 1, current_sum + nums[i], k_remaining):
                    return True
                used[i] = False

                # 关键剪枝：如果 current_sum == 0，说明这个数字是当前子集的第一个元素
                # 如果它失败了，那么以这个数字开头的所有情况都会失败
                if current_sum == 0:
                    return False

                # 关键剪枝：如果 current_sum + nums[i] == target 但失败了，说明这条路不通
                if current_sum + nums[i] == target:
                    return False

        return False

    return backtrack(0, 0, k)

