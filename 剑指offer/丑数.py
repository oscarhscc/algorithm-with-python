'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if not index:
            return 0
        num =[1]
        # 分别定义2,3,5的系数
        x, y, z = 0, 0, 0
        for i in range(index-1):
            while 2*num[x]<=num[-1]:
                x+=1
            while 3*num[y]<=num[-1]:
                y+=1
            while 5*num[z]<=num[-1]:
                z+=1
            num.append(min(2*num[x],3*num[y],5*num[z]))
        return num[-1]