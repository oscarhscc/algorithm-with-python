'''
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

'''
使用列表来装数据，然后进行求和
'''

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        numbers = []
        numbers.append(num1)
        numbers.append(num2)
        return sum(numbers)