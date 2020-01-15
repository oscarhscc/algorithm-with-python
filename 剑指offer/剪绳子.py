'''
题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
输出描述:
输出答案。
示例1
输入
8
输出
18
'''

'''
用动态规划来解决，首先定义一个dp列表，绳子不剪的话就是原来的长度，所以就是dp = [i for i in range(number + 1)]
然后我们可以求出递推公式res = dp[j] * dp[i-j]和原先的结果进行比较去最大的，最后的数就是结果。
'''

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if not number:
            return 0
        if number == 1:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        dp = [i for i in range(number + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(4, number + 1):
            result = 0
            for j in range(1, i):
                res = dp[j] * dp[i-j]
                result = max(res, result)
                dp.append(result)
        return dp[-1]