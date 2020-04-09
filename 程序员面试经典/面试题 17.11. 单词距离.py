'''
有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：

输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1
提示：

words.length <= 100000
通过次数1,673提交次数2,476
'''

class Solution(object):
    def findClosest(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1,i2 = [],[]
        for i in range(len(words)):
            if words[i] == word1:
                i1.append(i)
            if words[i] == word2:
                i2.append(i)
        min = len(words)
        for j1 in i1:
            for j2 in i2:
                if abs(j1 - j2) < min:
                    min = abs(j1 - j2)
        return min