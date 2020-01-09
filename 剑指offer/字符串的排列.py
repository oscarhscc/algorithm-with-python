'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        if len(ss) == 1: 
            return [ss]
        ret = []
        l = list(ss)
        l.sort()
        ss = "".join(l)
        previous = None
        for i in range(len(ss)):
        	# 如果有重复的字符，就跳下一个
            if previous == ss[i]:
                continue
            else:
            	# 给前一个字符进行赋值
                previous = ss[i]
            # 递归剩下的字符生成结果
            res = self.Permutation(ss[:i] + ss[i+1:])
            for k in res:
                ret.append(ss[i] + k)
        return ret