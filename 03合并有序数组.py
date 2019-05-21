'''
问题简述：给定两个有序整数数组num1和num2，将num2合并到num1，
使得num1成为一个有序数组（假设num1有足够的空间）

样例:
输入：num1=[1,2,3,0,0,0],m=3,num2=[2,5,6],n=3
输出：[1,2,2,3,5,6]
'''

class Solution:
#方法一：
    def merge1(self,num1,num2):
        mg = list()
        length1 = len(num1)
        length2 = len(num2)
        i1 = 0
        i2 = 0
        while i1<length1 and i2<length2:
            if num1[i1] < num2[i2]:
                mg.append(num1[i1])
                i1 += 1
            elif num1[i1] > num2[i2]:
                mg.append(num2[i2])
                i2 += 1
            else:
                mg.append(num1[i1])
                mg.append(num2[i2])
                i1 += 1
                i2 += 1

        if i1 == length1 and i2 != length2:
            mg = mg + num2[i2:]
        elif i2 == length2 and i1 != length1:
            mg = mg + num1[i1:]

        print(mg)
        return


#方法二：逆向扫描1

    def merge2(self,num1,m,num2,n):     #m,n分别是num1和num2的有效长度
        tail = n+m -1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            if num1[m] > num2[n]:
                num1[tail] = num1[m]
                m -= 1
                tail -= 1
            elif num1[m] < num2[n]:
                num1[tail] = num2[n]
                n -= 1
                tail -= 1
            else:
                num1[tail] = num1[m]
                tail -= 1
                m -= 1
                num1[tail] = num2[n]
                tail -= 1
                n -= 1

        if n >= 0 and m < 0:
            num1[:n] = num2[:n]
        print(num1)
        return

#逆向扫描2（标准答案）

    def merge3(self,num1,m,num2,n):
        while n > 0:                              #只管排num2，num2位置都对了，num1就不用管了，因为是有序的
            if m > 0 and num1[m-1] > num2[n-1]:
                num1[m+n-1] = num1[m-1]
                m -= 1
            else:
                num1[m+n-1] = num2[n-1]
                n -= 1
        print(num1)
        return





if __name__ == '__main__':
    num1 = [1,2,3,10,0,0,0]
    num2 = [2,5,6]

    s = Solution()
    s.merge3(num1,4,num2,3)

