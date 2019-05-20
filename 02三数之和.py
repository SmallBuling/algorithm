'''
问题简述：给定一个包含N个整数的数组，判断数组中是否存在三个元素a,b,c，使得a+b+c=0？
找出所有满足条件且不重复的三元组
样例：
nums = [-1,0,1,2,-1.-4]
满足要求的三元组集合为：[[-1,0,1],[-1,-1,2]]
'''
'''
方法：双指针法
1.先遍历，固定每一个元素
2.取第i个元素的后一个索引（i+1）为left指针，最后一个位置（len(list)-1）为right指针
3.因为list已经排序过，是有序的，故可以按照下面实现
if i+left+right == 0，append
  elif             < 0, left++
  elif             >0, right--
'''
class Solution:
    def ThreeSum(self,nums):
        res = list()
        nums.sort()
        for i,v in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:   #num[i:]是num[i-1:]的子集，避免重复
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:            #这三个if就是前面sort的原因，方便left和right指针的移动
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:   #i+left+right=0，i不变，如果left对应的值也不变，则right的值就固定了
                        left += 1                                        #这里需要一直找到跟原来的left不一样的nums的值，
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = [-2,0,1,1,2]
    print(s.ThreeSum(nums1))
