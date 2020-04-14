'''
假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

示例 1:

输入:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
输出: [7,10]
示例 2:

输入:
big = [1,2,3]
small = [4]
输出: []
'''

class Solution(object):
    def shortestSeq(self, big, small):
        """
        :type big: List[int]
        :type small: List[int]
        :rtype: List[int]
        """
        import collections
        cnt = collections.Counter(small)
        print(cnt)
        l = 0
        n = 0
        ans = []
        for r, ch in enumerate(big):
            if ch not in cnt:   #不在cnt 继续
                continue
            cnt[ch] -= 1         #在cnt
            if cnt[ch] == 0:
                n += 1          #统计n
            while big[l] not in cnt or cnt[big[l]] < 0: #移动左指针：big[l]不在cnt，或者big[l]出现不止一次
                if cnt[big[l]] < 0:
                    cnt[big[l]] += 1    #如果出现不止一次， 左指针右移，并加一
                l += 1
            if n == len(cnt):          #如果符合题目条件：
                if not ans or (ans[1]-ans[0]) > r - l:   #找最小串
                    ans = []
                    ans.append(l)
                    ans.append(r)
        return ans