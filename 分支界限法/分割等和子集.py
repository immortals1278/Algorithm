nums = list(map(int,input().split()))

nums.sort(reverse = True)

def func(nums):
    if len(nums) == 1:
        return "false"
    sum = 0
    for i in nums:
        sum += i
    if nums[0] > sum / 2:
        return "false"
    if sum % 2 != 0:
        return "false"

    lst = nums.copy()
    s = 0
    i = 0
    k = 1
    SUM = 0
    j = len(nums) - 1
    while s < sum / 2 :
        if i >= j :
            break

        if k %2 == 1:
            s += nums[i]
            lst.remove(nums[i])
            i += 1
        if k %2 == 0:
            s += nums[j]
            lst.remove(nums[j])
            j -= 1
        k += 1
    for i in lst:
        SUM += i

    if SUM == sum / 2:
        return "true"
    return "false"
print(func(nums))



