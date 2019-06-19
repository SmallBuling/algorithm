'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
'''

class  Solution:
    def mergeSortedArrays(self,nums1,nums2):
        i1 = 0
        i2 = 0
        merge = list()
        while i1<len(nums1) and i2< len(nums2):
            if nums1[i1] < nums2[i2]:
                merge.append(nums1[i1])
                i1 += 1
            else:
                merge.append(nums2[i2])
                i2 += 1
        if i1 == len(nums1):
            merge = merge + nums2[i2:]
        else:
            merge = merge + nums1[i1:]

        return merge



    def findMedianSortedArrays(self,nums1,nums2)->float:
        merge = self.mergeSortedArrays(nums1,nums2)
        print(merge)
        if len(merge)%2 == 1:
            return merge[len(merge)//2]
        else:
            return (merge[len(merge)//2]+merge[len(merge)//2-1])/2


if __name__ == '__main__':
    s = Solution()
    n1 = [1,2,3,4]
    n2 = [4,5,6]
    print(s.findMedianSortedArrays(n1,n2))