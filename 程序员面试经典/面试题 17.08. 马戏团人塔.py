'''
有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

示例：

输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
提示：

height.length == weight.length <= 10000
'''

class Solution(object):
    def bestSeqAtIndex(self, height, weight):
        """
        :type height: List[int]
        :type weight: List[int]
        :rtype: int
        """
        if not height: return 0
        length = len(height)
        actors = [(height[i], weight[i]) for i in range(length)]
        actors.sort(key=lambda x:(x[0], -x[1]))
        tail = [0] * length
        size = 0
        for actor in actors:
            i, j = 0, size
            while (i != j):
                mid = (i + j) // 2
                if tail[mid] < actor[1]: 
                    i = mid + 1
                else: 
                    j = mid            
            tail[i] = actor[1]
            if i == size: 
                size += 1
        return size