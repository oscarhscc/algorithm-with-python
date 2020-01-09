'''
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''

# 解法1 遍历所有的数，然后遍历字符进行统计
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        if n == 1:
            return 1
        for num in range(1, n + 1):
            data = str(num)
            for i in range(len(data)):
                if data[i] is '1':
                    count += 1
        return count


# 解法2 对于个位数：1每隔10次出现一次；十位数：每隔100出现10次；百位数：每隔1000出现100次；以此类推
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        temp = n
        res = 0
        base = 1 #出现次数
        while temp:
            p = temp % 10 #不完整部分
            temp = temp / 10
            res += temp * base #乘出现次数
            if p == 1:
                res += n % base + 1
            elif p > 1:
                res += base
            base*=10
        return res