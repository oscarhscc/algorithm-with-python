'''
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

# 这里需要两个栈，一个输入队列，一个输出队列，入栈是进入输入队列，输出是从输入队列到输出队列再从输出队列出栈。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
    def push(self, node):
        # write code here
        self.stack_in.append(node)
    def pop(self):
        # return xx
        if self.stack_out==[]:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        return self.stack_out.pop()