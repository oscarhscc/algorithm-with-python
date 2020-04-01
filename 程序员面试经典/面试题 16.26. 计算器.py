'''
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        pattern = re.compile(r'[*/+-]')
        s = s.strip()
        nums = re.split(pattern, s)
        syms = []
        for i in s:
            if i in ['+', '-', '*', '/']:
                syms.append(i)
        a = 0
        while a < len(syms):
            if syms[a] != '*' and syms[a] != '/':
                a += 1
            else:
                if syms[a] == '*':
                    nums[a] = int(nums[a]) * int(nums[a + 1])
                    nums.pop(a + 1)
                    syms.pop(a)
                else:
                    nums[a] = int(nums[a])//int(nums[a+1])
                    nums.pop(a+1)
                    syms.pop(a)
        res = int(nums[0])
        for i in range(len(syms)):
            if syms[i] == '+':
                res += int(nums[i + 1])
            else:
                res -= int(nums[i + 1])
        return res