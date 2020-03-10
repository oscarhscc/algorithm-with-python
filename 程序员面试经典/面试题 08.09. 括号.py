'''
括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return ['']
        res =[]
        for i in self.generateParenthesis(n-1):
            res.append("(" + i + ")")
        
        for i in range(1,n):
            for a in self.generateParenthesis(i):
                for b in self.generateParenthesis(n-i):
                    if a+b not in res:
                        res.append(a+b)
        return res