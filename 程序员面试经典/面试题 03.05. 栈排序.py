'''
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

示例1:

 输入：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
 输出：
[null,null,null,1,null,2]
示例2:

 输入： 
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
 输出：
[null,null,null,null,null,true]
说明:

栈中的元素数目在[0, 5000]范围内。
'''

class SortedStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.swim(len(self.stack)-1)
            

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return
        self.stack[0], self.stack[-1] = self.stack[-1], self.stack[0]
        self.stack.pop()
        self.sink(0)


    def peek(self):
        """
        :rtype: int
        """
        return self.stack and self.stack[0] or -1


    def isEmpty(self):
        """
        :rtype: bool
        """
        return not self.stack
    

    def sink(self, index):
        n = len(self.stack)
        while 2*index+1 < n:
            j = 2*index+1
            if j < n-1 and self.stack[j] > self.stack[j+1]:
                j += 1
            if self.stack[index] <= self.stack[j]:
                break
            self.stack[index], self.stack[j] = self.stack[j], self.stack[index]
            index = j
            
    
    def swim(self, index):
        while index > 0 and self.stack[index] < self.stack[(index-1)//2]:
            self.stack[index], self.stack[(index-1)//2] = self.stack[(index-1)//2], self.stack[index]
            index = (index-1)//2
            

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()