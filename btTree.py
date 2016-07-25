import math

class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def isLeftChild(self):
        if self.parent and self.parent.left == self:
            return True
        return False

    def isRightChild(self):
        if self.parent and self.parent.right == self:
            return True
        return False

    def isLeaf(self):
        if self.left == None and self.right == None:
            return True
        return False

class BTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if self.root == None:
            self.root = Node(value, self.root)
        else:
            if value < root.value:
                if root.left == None:
                    root.left = Node(value, root)
                else:
                    self.insert(root.left, value)
            else:
                if root.right == None:
                    root.right = Node(value, root)
                else:
                    self.insert(root.right, value)

    def findNode(self, root, value):
        node = None
        if root:
            if root.value == value:
                node = root
            else:
                if value < root.value:
                    node = self.findNode(root.left, value)
                else:
                    node = self.findNode(root.right, value)
        return node

    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print root.value
            self.inOrder(root.right)

    def findMin(self, node):
        if self.root and node:
            while node.left != None:
                node = node.left
            return node

    def findSuccessor(self, node):
        succ = None
        if self.root and node:
            if node.right:
                succ = self.findMin(node.right)
            else:
                if node.parent:
                    if node.isLeftChild():
                        succ = node.parent
                    else:
                        node.parent.right = None
                        succ = self.findSuccessor(node.parent)
                        node.parent.right = node
            return succ

    def delete(self, value):
        node = self.findNode(self.root, value)
        if node:
            if None not in (node.left, node.right):
                succ = self.findSuccessor(node)
                node.value = succ.value
                node = succ

            #leaf node
            if node.isLeaf():
                if node.isLeftChild():
                    node.parent.left = None
                else:
                    node.parent.right = None
            #Has only one child
            elif None in (node.left, node.right):
                if node.left:
                    node.value = node.left.value
                    node.left = None
                else:
                    node.value = node.right.value
                    node.right = None

    def depth(self, root):
        if root == None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root):
        if abs(self.depth(root.left) - self.depth(root.right)) > 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return False
        return True

    def isBalancedOptimalHelper(self, root):
        if root == None:
            return 0

        heightLeft = self.isBalancedOptimalHelper(root.left)
        if heightLeft == -1:
            return -1
        heightRight = self.isBalancedOptimalHelper(root.right)
        if heightRight == -1:
            return -1

        if abs(heightLeft - heightRight) > 1:
            return -1
        else:
            return 1 + max(heightRight, heightLeft)

    def isBalancedOptimal(self, root):
        if self.isBalancedOptimalHelper(root) == -1:
            return False
        else:
            return True

def BTreeFromSortedArray(arr, t2):
    if len(arr) > 2:
        pivotVal = len(arr)//2
        pivot = arr[pivotVal]
        t2.insert(t2.root, pivot)
        print arr[pivotVal]
        BTreeFromSortedArray(arr[0:pivotVal], t2)
        BTreeFromSortedArray(arr[pivotVal:], t2)

    return t2

# t1 = BTree()
# l = [15,3,2,1,66,10,4,9,17,67,13, 54]
# for item in l:
#     t1.insert(t1.root , item)
# t1.inOrder(t1.root)
# print "details"
# print t1.root.value
# print t1.findMin(t1.root).value
# print t1.findSuccessor(t1.root).value
# # t1.delete(10)
# # t1.delete(66)
# t1.inOrder(t1.root)
# print t1.depth(t1.root.left)
# print t1.depth(t1.root.right)

# print t1.isBalanced(t1.root)
# print t1.isBalancedOptimal(t1.root)

t2 = BTree()
arr = [i for i in range(1,20)]

t2 = BTreeFromSortedArray(arr, t2)
print t2.isBalanced(t2.root)