'''
每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

在结果列表中，选择字典序最小的名字作为真实名字。

示例：

输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], 
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]
提示：

names.length <= 100000
'''

class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        # 预处理
        f, cnt = {}, {}
        for name in names:
            n, c = name.split("(")
            f[n], cnt[n] = n, int(c[:-1])
        
        # 并查集查找同类根
        def find(x):
            if f[x] <> x: f[x] = find(f[x])
            return f[x]

        for synonym in synonyms:
            name1, name2 = synonym.split(",")
            # 如果当前同类名不在公布名单中，则跳过
            if f.get(name1[1:]) is None or f.get(name2[:-1]) is None: continue
            p1, p2 = find(name1[1:]), find(name2[:-1])
            # 保证同类根的字典序最小
            if p1 > p2: f[p1] = p2
            else: f[p2] = p1
        
        # 统计总频率
        ans = collections.defaultdict(int)
        for k, v in f.iteritems():
            ans[find(v)] += cnt[k]
        
        return [k+'('+str(v)+')' for k, v in ans.iteritems()]