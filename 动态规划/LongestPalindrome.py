s = input()


def longestPalindrome(s):
    res = ""  # 存储最长回文子串
    for i in range(len(s)):  # 遍历每个字符作为中心
        # 奇数长度回文（中心是一个字符）
        a, b = i, i  # 左右指针都指向中心i
        while a >= 0 and b < len(s) and s[a] == s[b]:  # 如果左右字符相等
            if b - a + 1 > len(res):  # 如果当前回文更长
                res = s[a:b + 1]  # 更新结果
            a -= 1  # 左指针向左移
            b += 1  # 右指针向右移

        # 偶数长度回文（中心是两个字符之间）
        a, b = i, i + 1  # 左指针i，右指针i+1
        while a >= 0 and b < len(s) and s[a] == s[b]:
            if b - a + 1 > len(res):
                res = s[a:b + 1]
            a -= 1
            b += 1

    return res


print(longestPalindrome(s))
