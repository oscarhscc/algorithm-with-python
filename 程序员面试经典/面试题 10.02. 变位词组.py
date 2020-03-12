'''
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

注意：本题相对原题稍作修改

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        position = {}
        result = []
        count = 0
        for term in strs:
            sorted_term = "".join(sorted(term))
            if sorted_term not in position.keys():
                result.append([term])
                position[sorted_term] = count
                count += 1
            else:
                result[position[sorted_term]].append(term)
        return result