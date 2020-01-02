'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''

'''
这是一种递归写法，很容易读懂，但是这种递归计算量巨大，一般来说这种递归的方法无法使用，需要大量的重复计算时间复杂度爆炸。

class Solution(object):
	"""docstring for Solution"""
	def Fibonacci(self, n):
		n = 0
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n > 1:
			num = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
		return num
'''

class Solution(object):
	"""docstring for ClassName"""
	def Fibonacci(self, n):
		a, b = 1, 0
		for i in range(n + 1):
			a, b = b, a + b
		return a
