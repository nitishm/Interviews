import math

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0 or x < self.stack[-1][1]:
             self.stack.append((x,x))
        else:
            self.stack.append((x,self.stack[-1][1]))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return None

        ret = self.stack[-1]
        self.stack = self.stack[0:len(self.stack) - 1]
        return ret[0]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[0][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.push(1)
# print "POP", obj.pop()
print obj.getMin()
# param_3 = obj.top()
# param_4 = obj.getMin()