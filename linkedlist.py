# -*- coding: utf-8 -*-
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        curNode = self.head
        index = 0

        op = "^ -> "
        while curNode != None:
            op = op + str(curNode.getData()) + " -> "
            curNode = curNode.getNext()
            index = index + 1
        return op + '$'


    def add(self, data):
        node = Node(data)
        node.setNext(self.head)
        self.head = node

    def size(self):
        count = 0
        curNode = self.head
        while curNode != None:
            count = count + 1
            curNode = curNode.getNext()
        return count

    def remove(self, data):
        prevNode = None
        curNode = self.head
        while curNode != None:
            if curNode.getData() == data:
                if prevNode == None:
                    self.head = curNode.getNext()
                else:
                    prevNode.setNext(curNode.getNext())
            prevNode = curNode
            curNode = curNode.getNext()

    def append(self, data):
        if self.size() == 0:
            self.add(data)
            return
        curNode = self.head
        while curNode.getNext() != None:
            curNode = curNode.getNext()
        node = Node(data)
        curNode.setNext(node)

    def insert(self, data, pos):
        if pos == 0:
            self.add(data)
        elif pos < 0 or pos > self.size():
            print "ERROR: pos error"
            return
        elif pos == self.size():
            self.append(data)
        else:
            curNode = self.head
            prevNode = None
            index = 0
            while curNode != None and index != pos:
                index = index + 1
                prevNode = curNode
                curNode = curNode.getNext()
            node = Node(data)
            prevNode.setNext(node)
            node.setNext(curNode)

    def index(self, data):
        pass

    def pop(self, pos = 0):
        if pos < 0 or pos >= self.size():
            print "ERROR: pos error"
            return
        
        if pos == 0:
            self.head = self.head.getNext()
            return 

        prevNode = None
        curNode = self.head
        index = 0
        while curNode != None and pos != index:
            prevNode = curNode
            curNode = curNode.getNext()
            index = index + 1
        prevNode.setNext(curNode.getNext())

    def reverse(self):
        curNode = self.head
        while curNode.getNext() != None:
            temp = curNode.getNext()
            curNode.setNext(curNode.getNext().getNext())
            temp.setNext(self.head)
            self.head = temp
        return self

    def pad(self, num):
        if num <= 0:
            return self
        index = 0
        while index < num:
            self.insert(0, 0)
            index = index + 1
        return self

    def insertResult(self, sum):
        if self.size() == 0:
            self.add(0)
            self.tracker = self.head
        else:
            self.tracker.data = self.tracker.data + 1
            self.tracker.next = Node(sum % 10)
            self.tracker = self.tracker.next

    def partition(self, number):
        runner = self.head
        while runner.data < number and runner.next != None:
            runner = runner.next
        self.tail = runner
        partitionpoint = runner
        while runner != None:
            temp = runner
            runner = runner.next
            if temp.data < number:
                temp.next = self.head
                self.head = temp
            else:
                temp.next = None
                self.tail.next = temp
                self.tail = temp
        print "Partition point is ", partitionpoint.data

def addLinkedListRev(L1, L2):
    L1.pad(L2.size() - L1.size())
    L2.pad(L1.size() - L2.size())

    p1 = L1.head
    p2 = L2.head

    result = 0
    while p1 != None and p2 != None:
        result = (result * 10) + p1.getData() + p2.getData()
        p1 = p1.getNext()
        p2 = p2.getNext()
    resultList = LinkedList()
    for i in str(result):
        resultList.append(i)

    return resultList

def addLinkedListRev_ll(L1, L2):
    result = LinkedList()
    result.insertResult(0)
    p1, p2 = L1.head, L2.head
    while p1 != None and p2 != None:
        sum = p1.data + p2.data
        result.insertResult(sum)
        p1, p2 = p1.getNext(), p2.getNext()
    return result

def addLinkedListFwd(L1, L2):
    p1, p2 = L1.head, L2.head
    carry = 0
    sum = LinkedList()
    while p1 != None and p2 != None:
        sumNumber = p1.getData() + p2.getData() + carry
        sum.append(sumNumber % 10)
        carry = sumNumber // 10
        p1, p2 = p1.getNext(), p2.getNext()

    if carry:
        sum.append(carry)
    return sum

if __name__ == "__main__":
    # ll = LinkedList()
    # for item in [15, 12, 1, 17, 10]:
    #     ll.add(item)
    #     print ll
    # print "APPENDING"
    # ll.append(22)
    # print ll
    # print "INSERTING"
    # ll.insert(65, 0)
    # print ll
    # ll.insert(76, ll.size())
    # print ll
    # ll.insert(777, 3)
    # print ll
    # print "POPPING"
    # ll.pop(0)
    # print ll
    # ll.pop(ll.size() - 1)
    # print ll
    # ll.pop()
    # print ll

    L1 = LinkedList()
    L2 = LinkedList()
    for item in [7,8,9]:
        L1.append(item)
    for item in [6, 5, 3]:
        L2.append(item)

    result = addLinkedListRev(L1, L2)
    print "1)", result
    result = addLinkedListRev_ll(L1, L2)
    print "2)", result
    result = addLinkedListFwd(L1.reverse(), L2.reverse())
    print "3)", result

    L3 = LinkedList()
    for item in [5,10,2,3,11,9,1,7,8]:
        L3.append(item)

    print L3
    L3.partition(8)
    print L3