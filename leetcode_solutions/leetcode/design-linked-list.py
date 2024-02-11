class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0
    def get(self, index: int) -> int:
        if index > self.count -1: return(-1)
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val 
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.count+=1

    def addAtTail(self, val: int) -> None:
        if self.count == 0: self.addAtHead(val)
        else: self.addAtIndex(self.count,val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count: return -1

        if index == 0:
            self.addAtHead(val)
            self.count += 1
            return
        
        node = Node(val)
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        self.count += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index>= self.count: return
        cur =  self.head
        if index == 0: self.head = self.head.next
        else:
            for i in range(index-1):
                cur = cur.next
            cur.next = cur.next.next
        self.count -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)