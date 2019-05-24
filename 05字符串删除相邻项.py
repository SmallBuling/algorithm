'''
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

思路：用栈实现，遍历str，如果栈为空，则入栈，如果栈顶元素和字符串元素相等，则stack.pop栈顶元素，如果不等，就入栈
'''
'''
join函数：
作用： 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
语法：  'sep'.join(seq)

参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串

返回值：返回一个以分隔符sep连接各个元素后生成的字符串
'''
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        i = 0
        while i < len(S):
            if stack:
                if stack[len(stack)-1] == S[i]:
                    stack.pop()
                else:
                    stack.append(S[i])
            else:
                stack.append(S[i])
            i += 1
        return "".join(stack)






if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates('abbac'))


