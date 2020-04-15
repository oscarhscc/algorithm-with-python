'''
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。

编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
'''

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[str]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            print('not in')
            return []
        temp = []
        def get_res(word):
            # print(word)
            if word == endWord:
                return True
            elif len(word_set) == 0:
                return False
            for i in range(len(word)):
                ch = word[i]
                del_words = []
                for j in range(26):
                    n_ch = chr(ord('a') + j)
                    n_word = word[:i] + n_ch + word[i + 1:]
                    if n_ch == ch or n_word not in word_set:
                        continue
                    word_set.remove(n_word)
                    temp.append(n_word)
                    if get_res(n_word):
                        return True
                    else:
                        del_words.append(n_word)
                        # word_set.add(n_word)
                        del temp[-1]
            word_set.update(del_words)
        get_res(beginWord)
        return temp if temp == [] else [beginWord] + temp