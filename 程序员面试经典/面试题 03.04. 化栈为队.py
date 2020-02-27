'''
实现一个MyQueue类，该类用两个栈来实现一个队列。

示例：

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
'''

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.s1:
            tmp = self.s1.pop()
            self.s2.append(tmp)
        res = self.s2.pop()
        while self.s2:
            tmp = self.s2.pop()
            self.s1.append(tmp)
        return res


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.s1:
            tmp = self.s1.pop()
            self.s2.append(tmp)
        res = self.s2[-1]
        while self.s2:
            tmp = self.s2.pop()
            self.s1.append(tmp)
        return res


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1)==0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()