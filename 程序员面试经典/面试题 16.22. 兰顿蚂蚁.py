'''
一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。

(1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。
(2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。

编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。

网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 'X' 表示，白色方格由 '_' 表示，蚂蚁所在的位置由 'L', 'U', 'R', 'D' 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。

示例 1:

输入: 0
输出: ["R"]
示例 2:

输入: 2
输出:
[
  "_X",
  "LX"
]
示例 3:

输入: 5
输出:
[
  "_U",
  "X_",
  "XX"
]
说明：

K <= 100000
'''

class Solution(object):
    def printKMoves(self, K):
        """
        :type K: int
        :rtype: List[str]
        """
        color = '_'
        res = ['_']
        d = 'R'
        now = [0, 0]
        while K > 0:
            K -= 1
            if d == 'R':
                if color == '_':
                    res[now[0]] = res[now[0]][:now[1]] + 'X' + res[now[0]][now[1]+1:]
                    if now[0] == len(res)-1:
                        res.append('_'*len(res[0]))
                    d = 'D'
                    now[0] += 1
                    color = res[now[0]][now[1]]
                else:
                    res[now[0]] = res[now[0]][:now[1]] + '_' + res[now[0]][now[1]+1:]
                    if now[0] == 0:
                        res.insert(0, '_'*len(res[0]))
                        now[0] += 1
                    d = 'U'
                    now[0] -= 1
                    color = res[now[0]][now[1]]
            elif d == 'L':
                if color == '_':
                    res[now[0]] = res[now[0]][:now[1]] + 'X' + res[now[0]][now[1]+1:]
                    if now[0] == 0:
                        res.insert(0, '_'*len(res[0]))
                        now[0] += 1
                    now[0] -= 1
                    d = 'U'
                    color = res[now[0]][now[1]]
                else:
                    res[now[0]] = res[now[0]][:now[1]] + '_' + res[now[0]][now[1]+1:]
                    if now[0] == len(res)-1:
                        res.append('_'*len(res[0]))
                    d = 'D'
                    now[0] += 1
                    color = res[now[0]][now[1]]
            elif d == 'U':
                if color == '_':
                    res[now[0]] = res[now[0]][:now[1]] + 'X' + res[now[0]][now[1]+1:]
                    if now[1] == len(res[0]) - 1:
                        for i in range(len(res)):
                            res[i] += '_'
                    d = 'R'
                    now[1] += 1
                    color = res[now[0]][now[1]]
                else:
                    res[now[0]] = res[now[0]][:now[1]] + '_' + res[now[0]][now[1]+1:]
                    if now[1] == 0:
                        for i in range(len(res)):
                            res[i] = '_' + res[i]
                        now[1] += 1
                    d = 'L'
                    now[1] -= 1
                    color = res[now[0]][now[1]]
            else:
                if color == '_':
                    res[now[0]] = res[now[0]][:now[1]] + 'X' + res[now[0]][now[1]+1:]
                    if now[1] == 0:
                        for i in range(len(res)):
                            res[i] = '_' + res[i]
                        now[1] += 1
                    d = 'L'
                    now[1] -= 1
                    color = res[now[0]][now[1]]
                else:
                    res[now[0]] = res[now[0]][:now[1]] + '_' + res[now[0]][now[1]+1:]
                    if now[1] == len(res[0])-1:
                        for i in range(len(res)):
                            res[i] += '_'
                    d = 'R'
                    now[1] += 1
                    color = res[now[0]][now[1]]
        res[now[0]] = res[now[0]][:now[1]] + d + res[now[0]][now[1]+1:]
        return res
