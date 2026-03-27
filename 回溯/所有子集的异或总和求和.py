def dfs(nums, i, cur_xor):
    if i == len(nums):
        return cur_xor
    return dfs(nums, i+1, cur_xor ^ nums[i]) + dfs(nums, i+1, cur_xor)
# 有可能到最后一个元素cur一个没xor，也可能全xor

nums = list(map(int, input().split()))
print(dfs(nums, 0, 0))