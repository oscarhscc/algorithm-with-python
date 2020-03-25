'''
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：

输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：

输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：

输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：

0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
'''

class Solution(object):
    def patternMatching(self, pattern, value):
        """
        :type pattern: str
        :type value: str
        :rtype: bool
        """
        if not value and not pattern: 
            return True
        if not pattern: 
            return False
        if not value:
            if len(pattern)==1: 
                return True
            else: 
                return False
        if len(set(pattern))==1: # 如果只有一种pattern
            if len(value)%len(pattern)!=0:
                return False
            length = len(value) // len(pattern)
            return all([value[i:i+length]==value[0:length] for i in range(0, len(value),length)])

        if pattern.count('a')==1 or pattern.count('b')==1:# 两种pattern但是其中一种只有一个，只需要另这个为value，另外一个为空即可
            return True
        
        cnt_a = pattern.count('a')
        cnt_b = pattern.count('b')
        for i in range(len(value)//cnt_a): # 遍历a的所有可能长度
            remain = len(value) - i * cnt_a 
            if remain % cnt_b != 0:
                continue
            j = remain // cnt_b
            set_a = set()
            set_b = set()
            p = 0
            for s in pattern:
                if s=='a':
                    set_a.add(value[p:p+i])
                    p += i
                else:
                    set_b.add(value[p:p+j])
                    p += j
            if len(set_a)==len(set_b)==1:
                return True
        return False