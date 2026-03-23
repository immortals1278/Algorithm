def longestSubstring(s, k):
    if len(s) < k:
        return 0

    # 统计s中每个字符出现次数
    from collections import Counter
    count = Counter(s) # Counter({'a': 3, 'b': 2})

    # 先判断整个s是不是最大子串（有分割点就不是），每次分割判断一次
    # 找到出现次数小于k的字符作为分割点
    for char, num in count.items():# num是值，char是键
        if num < k:
            # 以该字符分割，分别计算左右子串
            return max(longestSubstring(sub, k) for sub in s.split(char))

    # 所有字符出现次数都>=k，返回整个字符串长度
    return len(s)


# 读取输入
s, k = input().split()
k = int(k)

# 输出结果
print(longestSubstring(s, k))