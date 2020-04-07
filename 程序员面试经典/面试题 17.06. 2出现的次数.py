'''
编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。

示例:

输入: 25
输出: 9
解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
提示：

n <= 10^9
'''

class Solution(object):
    def numberOf2sInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0;
        i=1
        while i<=n:
            temp = (n//i) ##一般count计数
            cur = temp%10  ##当前位数
            temp1 = temp//10 ##一般count计数
            temp2 = n%i      ##边界count
            ans += temp1*i   
            if(cur == 2):
                ans += temp2+1   
            if(cur>2):
                ans += i
            i = i*10
        return ans