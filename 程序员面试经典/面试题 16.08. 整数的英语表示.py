'''
给定一个整数，打印该整数的英文描述。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4:

输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        unit = [('Billion', int(10 ** 9)), ('Million', int(10 ** 6)), ('Thousand', 1000), ('Hundred', 100)]
        memo = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        ten = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',  'Seventy', 'Eighty', 'Ninety']
        if num < 20: 
        	return memo[num]
        ans = ''
        for i, u in unit:
            if num // u > 0:
                ans += self.numberToWords(num // u) + ' ' + i + ' '
            num = num % u
        if num == 0: 
            return ans.strip()
        if num < 20: 
            ans += memo[num]
        else: 
            ans += ten[num // 10 - 2] + (' ' + memo[num % 10] if num % 10 != 0 else '')
        return ans