#问题简述：给定一个数组，返回两个数字的下标，其中两个数字之和等于给定的目标值（假设有且只有一个解）
#样例：num = [2,7,11,15]   target = 9，则返回[0,1]

class Solution(object):
#方法一：暴力枚举
    def TwoSum1(self,nums,target):
        # enumerate 可以将数据对象的下标和数据同时列举出来，一般用于for循环中
        for i,n in enumerate(nums):                  #i代表下标，遍历nums
            for j in  range(i+1,len(nums)):          #从i的后一个元素开始遍历相加
                if nums[i]+nums[j] == target:
                    return i,j

#方法二：使用哈希函数
#思路：暴力枚举的内层循环的目的是为了查找数组中target-n的元素，
#对于外层循环的每一个元素，都要查找一遍，可采用哈希函数加快查找
#的速度

    def TwoSum2(self,nums,target):
        numidx = dict()
        for i,n in enumerate(nums):
            if target-n in numidx:
                return numidx[target-n],i
            else:
                numidx[n] = i

#---------------------下面3和4的算法是我自己改编的，正确性可待商榷，但是感觉算法4很棒！！！！！！！！
    def TwoSum3(self,nums,target):
        numidx = list()
        for i,n in enumerate(nums):
            if target-n in numidx:
                return numidx.index(target-n),i
            else:
                numidx.insert(i,n)

    def TwoSum4(self,nums,target):
        for i,n in enumerate(nums):
            # nums.index(target-n) != i 防止出现target是某个元素的两倍的情况，如target=6,nums = [3,2,4]就会报错
            if target-n in nums and nums.index(target-n) != i:
                return nums.index(target-n),i

num = [2,7,11,15]
num1 = [3,2,4,4]

a = Solution()
print(a.TwoSum1(num,26))
print(a.TwoSum2(num,9))
print(a.TwoSum4(num1,8))