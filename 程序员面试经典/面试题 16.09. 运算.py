'''
请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。

你的实现应该支持如下操作：

Operations() 构造函数
minus(a, b) 减法，返回a - b
multiply(a, b) 乘法，返回a * b
divide(a, b) 除法，返回a / b
示例：

Operations operations = new Operations();
operations.minus(1, 2); //返回-1
operations.multiply(3, 4); //返回12
operations.divide(5, -2); //返回-2
提示：

你可以假设函数输入一定是有效的，例如不会出现除法分母为0的情况
单个用例的函数调用次数不会超过1000次
'''

class Operations(object):

    def __init__(self):
        pass

    def calSign(self, a, b):
        pos = True
        if a < 0:
            pos = not pos
            a = self.minus(0, a)
        if b < 0:
            pos = not pos
            b = self.minus(0, b)
        return (a, b, pos)

    def minus(self, a, b):
        # 不用位运算 - 借助str
        if b < 0:
            b = int(str(b)[1:])
        else:
            b = int('-' + str(b))
        return a + b

    def multiply(self, a, b):
        # 不用位运算, 十进制乘法, 需要借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        sb = str(b)
        zerobits = 0
        for c in sb[::-1]:
            n = int(c)
            cur = 0
            for i in range(n):
                cur += a
            cur = int(str(cur) + '0' * zerobits)
            zerobits += 1
            res += cur
        return res if pos else self.minus(0, res)

    def divide(self, a, b):
        # 十进制除法, 借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        cur = 0
        for c in str(a):
            cur = self.multiply(10, cur) + int(c)
            cnt = 0
            while cur >= b:
                cur = self.minus(cur, b)
                cnt += 1
            res = self.multiply(10, res) + cnt
        return res if pos else self.minus(0, res)



# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)