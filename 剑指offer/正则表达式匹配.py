'''
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if (len(s) == 0 and len(pattern) == 0):
            return True
        if (len(s) > 0 and len(pattern) == 0):
            return False
        # pattern 第一位是*通配符的情况下
        if (len(pattern) > 1 and pattern[1] == '*'):
        	# 第一个字符匹配
            if (len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.')):
            	# 1.*后面这个字符没有，从pattern第三个字符开始匹配
        		# 2.*后面这个字符出现一次，从s第二个字符和pattern第三个字符开始匹配
        		# 3.前两个字符一样，从s第二个字符开始匹配
                return (self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern))
            else:
            	# pattern 第二个字符没有出现，直接从第三个字符开始匹配
                return self.match(s, pattern[2:])
        if (len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0])):
        	# 第一个字符匹配，从第二个字符开始匹配
            return self.match(s[1:], pattern[1:])
        return False