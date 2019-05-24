'''
判断一个整数是否是回文数，回文数是指正序（从左到右）和倒叙（从后到左）读都是一样的整数
样例1：
输入：121
输出：True
样例2：
输入：-121
输出：False
样例3：
输入：10
输出：False
'''

class Solution:
#方法一：转换成字符串处理
    def isPalindrome(self,x):
        if x < 0:
            return False
        elif x >= 0 and x < 10:
            return True
        else:
            s = str(x)               #ex: x=12321 s="12321"
            l = list(s)              #  l = ['1','2','3','2','1']
            left = 0
            right = len(l) - 1
           # mid = int(len(l)/2)      #这里需要注意一下,python3的除的结果不是取整，可能会产生小数，用int可以向下取整,或者使用//取整符号
            mid = len(l) / 2
            while left < mid:
                if l[left] != l[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True

#方法二：
#思路：判断前半部分的数字与后半部分的数字是否相等
#例如123321
#前半部分（123）与后半部分(321)的反转（123）相等，即前半部分<=后半部分
#ps:这种解法对10的倍数的数字有bug，10的倍数也不可能是回文数，故在开始直接if就好

#
    def isPalindrome2(self, x):
        if x < 0 or (x%10 == 0 and x != 0):                   #注意这个边界条件
            return False
        else:
            left = x
            right = 0                                          #左边的43-50行代码可以改写下面这样
            while left >=  right:                              # while left >  right:
                if right == left:                              #    right = right*10 + left%10
                    return True                                #    left //= 10
                right = right*10 + left%10                     # return right == left or right//10 == left
                left //= 10
            if int(right/10) == left:
                return True
            return False




if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome2(1010))
