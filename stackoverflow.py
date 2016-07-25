class StackOverflow:
    def __init__(self, maxSize):
        self.stackOfStacks = []
        self.maxSize = maxSize

    def printStack(self):
        for stack in self.stackOfStacks:
            print "New stack"
            for item in stack:
                print item

    def push(self, item):
        if len(self.stackOfStacks) == 0 or len(self.stackOfStacks[-1]) == self.maxSize:
            stack = []
            stack.append(item)
            self.stackOfStacks.append(stack)
        else:
            self.stackOfStacks[-1].append(item)

    def pop(self):
        if len(self.stackOfStacks) == 0:
            print "Error : Empty stack"
            return None
        
        item = self.stackOfStacks[-1].pop()
        if len(self.stackOfStacks[-1]) == 0:
            self.stackOfStacks.pop()

        return item

so = StackOverflow(10)
so.push(1)
so.push(2)
so.push(3)
so.push(4)
so.push(5)
so.push(6)
so.push(7)
print "After push"
so.printStack()
so.pop()
so.pop()
so.pop()
so.pop()
so.pop()
so.pop()
so.pop()
so.pop()
print "After pop"
so.printStack()
