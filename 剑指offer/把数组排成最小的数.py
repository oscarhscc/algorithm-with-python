'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers.sort(cmp = self.lmp)
        return ''.join([str(i) for i in numbers])
        
    def lmp(self,n1,n2):
        if str(n1) + str(n2) > str(n2) + str(n1):
            return 1
        else:
            return -1