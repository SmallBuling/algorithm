'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 
的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
#方法1.遍历法
    def maxArea1(self, height):
        max = 0
        for i1,v1 in enumerate(height):                        #外层循环，宽的起点
            i2 = i1+1
            while i2<len(height):                              #内存循环，宽的终点，两者的差即是宽度
                tall=v1 if v1<height[i2] else height[i2]        #选取宽两边矮的那个作为高
                width = i2 - i1
                area = tall * width
                if area > max: max = area
                i2 += 1
        return max

#方法二：双指针法
#矩阵的面积与两个因素有关：

#矩阵的长度：两条垂直线的距离
#矩阵的宽度：两条垂直线其中较短一条的长度
#因此，要矩阵面积最大化，两条垂直线的距离越远越好，两条垂直线的最短长度也要越长越好。

#我们设置两个指针 left 和 right，分别指向数组的最左端和最右端。此时，两条垂直线的距离是最远的，
#若要下一个矩阵面积比当前面积来得大，必须要把 height[left] 和 height[right] 中较短的垂直线往中间移动，
#看看是否可以找到更长的垂直线。

#链接：https://leetcode-cn.com/problems/two-sum/solution/shuang-zhi-zhen-jie-fa-by-jalan/

    def maxArea2(self, height):
        maxarea = 0
        left = 0
        right = len(height)-1
        while right != left:
            width = right - left
            if height[right] > height[left]:
                tall = height[left]
                left += 1
            else:
                tall = height[right]
                right -= 1
            area = width*tall
            if area>maxarea: maxarea=area
        return maxarea


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea2(height))