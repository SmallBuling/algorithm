'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

class Solution:
    def lenthOfLongestSubstring1(self,s):
        longest = 0
        i1 = 0
        i2 = 0
        temp = list()
        while longest < (len(s[i1:])):
            i2 = i1
            temp.clear()
            while i2 < len(s) and s[i2] not in temp :    #这个地方需要把i2<len（s）放到前面，如果把s[i2]放到前面会发生越界错误
                temp.append(s[i2])
                i2 += 1
            if len(temp) > longest:
                longest = len(temp)
            i1 += 1

        return longest

#滑动窗口法    但是还是不懂
    def lenthOfLongestSubstring2(self,s):
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0     #目前set里面的元素长度

        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    s = Solution()
    str = "pwwkew"
    print(s.lenthOfLongestSubstring2(str))