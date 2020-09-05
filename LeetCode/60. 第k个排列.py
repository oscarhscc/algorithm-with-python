'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def func(x):
            # 计算阶乘
            res = 1
            for i in range(2, x+1):
                res *= i
            return res
        
        res = ""
        bar = func(n)
        # 记录还剩哪些数字没有选过
        nums = list(range(1,n+1))
        while len(res) != n:
            # 除当前位剩余位数的阶乘（表示总的可能的次数）
            bar /= (n-len(res))
            buf = 0
            # 循环，根据k值以及bar值，计算当前位的数字
            # 后来发现直接用除法就可以做了
            while k>bar:
                k -= bar
                buf += 1
            res += str(nums[buf])
            nums.pop(buf)
        return res