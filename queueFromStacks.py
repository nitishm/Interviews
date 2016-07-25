class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackOrig = []
        self.stackCopy = []
        
    
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stackOrig.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            raise "No elements found in queue"
            return None
        self.moveStackOrigToCopy()
        val = self.stackCopy[len(self.stackCopy) - 1]
        self.stackCopy = self.stackCopy[0:len(self.stackCopy) - 1]
        return val

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            raise "No elements found in queue"
            return None
        self.moveStackOrigToCopy()
        return self.stackCopy[len(self.stackCopy) - 1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stackOrig) + len(self.stackCopy) == 0:
            return True
        return False
        
    def moveStackOrigToCopy(self):
        if len(self.stackCopy) == 0:
            while len(self.stackOrig) != 0:
                self.stackCopy.append(self.stackOrig.pop())


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.pop()
q.pop()
q.pop()
#print q.peek()
print q.empty()
