'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

'''
因为每次可以跳1-n级台阶，那么我们假设在第n级台阶的跳法数为f(n)，
那么f(n) = f(n-1) + f(n-2) + ... + f(2) + f(1),
所以就有f(n-1) = f(n-2) + ... + f(2) + f(1),这样的话就有
f(n) = 2 * f(n-1)
'''

# 解法1
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return pow(2, number-1)


# 解法2
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        dp = [_ for _ in range(number + 1)]
        for i in range(2, number + 1):
            dp[i] = 2 * dp[i-1]
        return dp[-1]
