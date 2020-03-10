'''
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。
'''

class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return []
        if len(S) == 1:
            return [S]
        S = ''.join(sorted(list(S)))
        res = []
        def helper(cur_S='', rest_S=S):
            if len(rest_S) == 0:
                res.append(cur_S)
            for i in range(len(rest_S)):
                if i == 0:
                    helper(cur_S+rest_S[i], rest_S[:i]+rest_S[i+1:])
                elif i > 0 and rest_S[i] != rest_S[i-1]:
                    helper(cur_S+rest_S[i], rest_S[:i]+rest_S[i+1:])
        helper()
        return res