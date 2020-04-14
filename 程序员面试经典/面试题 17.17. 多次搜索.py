'''
给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，
根据smalls中的每一个较短字符串，对big进行搜索。
输出smalls中的字符串在big里出现的所有位置positions，
其中positions[i]为smalls[i]出现的所有位置。

示例：

输入：
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
提示：

0 <= len(big) <= 1000
0 <= len(smalls[i]) <= 1000
smalls的总字符数不会超过 100000。
你可以认为smalls中没有重复字符串。
所有出现的字符均为英文小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multi-search-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def multiSearch(self, big, smalls):
        """
        :type big: str
        :type smalls: List[str]
        :rtype: List[List[int]]
        """
        trie_tree = {}
        for i, word in enumerate(smalls):
            tree = trie_tree
            for c in word:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]
            tree[-1] = i
        res = [[] for _ in range(len(smalls))]
        for i in range(len(big)):
            tree = trie_tree
            for j in range(i, len(big)):
                if big[j] not in tree:
                    break
                tree = tree[big[j]]
                if -1 in tree:
                    res[tree[-1]].append(i)
        return res