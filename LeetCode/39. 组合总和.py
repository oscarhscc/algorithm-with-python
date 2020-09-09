'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(temp, res):
            if temp > target:#剪枝一:当前的总值大于目标值
                return
            if temp == target:#当前值和目标值相等的时候,保存当前结果,并返回
                result.append(res)
                return
            for i in candidates:
                if res and res[-1] > i:#防止重复的方法是,不让其找在当前元素以前的元素
                    continue
                dfs(temp + i, res + [i])
        dfs(0, [])
        return result