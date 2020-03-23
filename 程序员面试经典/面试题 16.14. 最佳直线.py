'''
给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。

设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。

示例：

输入： [[0,0],[1,1],[1,0],[2,0]]
输出： [0,2]
解释： 所求直线穿过的3个点的编号为[0,2,3]
提示：

2 <= len(Points) <= 300
len(Points[i]) = 2
'''

class Solution(object):
    def bestLine(self, points):
        """
        :type points: List[List[int]]
        :rtype: List[int]
        """
        size = len(points)
        if size <= 0:return []
        if size <= 1:return [0]
        def gcd(a,b):
            return a if b == 0 else gcd(b,a%b)
        def getlinestr(p1,p2):
            difx = p1[0] - p2[0]
            dify = p1[1] - p2[1]
            if difx == 0:
                return str(p1[0])+":0"
            if dify == 0:
                return "0:"+str(p1[1])
            g = gcd(dify,difx)
            k_u = dify / g
            k_d = difx / g
            c = k_d*p1[0] - k_u*p1[1]
            g = gcd(c,k_d)
            b_u = c/g
            b_d = k_d / g
            return str(k_u)+":"+str(k_d)+","+str(b_u)+":"+str(b_d)
        buff = dict()
        for i in range(size):
            for j in range(i+1,size):
                funstr = getlinestr(points[i],points[j])
                if funstr not in buff:
                    buff[funstr] = set()
                buff[funstr].add(i)
                buff[funstr].add(j)
        mx = 0
        ret = []
        for k in buff:
            v = buff[k]
            if len(v) > mx:
                ret = [list(v)]
                mx = len(v)
            elif len(v) == mx:
                ret.append(list(v))
        if mx > 0:
            for i in range(len(ret)):
                ret[i].sort()
            ret.sort()
            return ret[0][0:2]
        return []