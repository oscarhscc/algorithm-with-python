'''
堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。

当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1.

示例1:

 输入：
["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
[[1], [1], [2], [1], [], []]
 输出：
[null, null, null, 2, 1, -1]
示例2:

 输入：
["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
[[2], [1], [2], [3], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, 3]

'''

class StackOfPlates(object):

    def __init__(self, cap):
        """
        :type cap: int
        """
        self.cap = cap
        self.stacks = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.cap == 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)


    def pop(self):
        """
        :rtype: int
        """
        return self.popAt(len(self.stacks) - 1)


    def popAt(self, index):
        """
        :type index: int
        :rtype: int
        """
        if not self.stacks or index >= len(
                self.stacks) or not self.stacks[index]:
            return -1
        res = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks = self.stacks[0:index] + self.stacks[index + 1:]
        return res



# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)