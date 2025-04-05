class Node:
    def __init__(self, value= None):
        self.value = value
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        # Dummy node to simplify operations
        self.dummy = Node()  
        # Initially, the deque is empty so dummy points to itself.
        self.dummy.next = self.dummy  
        self.dummy.prev = self.dummy
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = Node(value)
        # Insert newNode right after dummy
        newNode.next = self.dummy.next
        newNode.prev = self.dummy
        self.dummy.next.prev = newNode
        self.dummy.next = newNode
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = Node(value)
        # Insert newNode right before dummy (at the rear)
        newNode.prev = self.dummy.prev
        newNode.next = self.dummy
        self.dummy.prev.next = newNode
        self.dummy.prev = newNode
        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # Remove the first element (dummy.next)
        first = self.dummy.next
        self.dummy.next = first.next
        first.next.prev = self.dummy
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # Remove the last element (dummy.prev)
        last = self.dummy.prev
        self.dummy.prev = last.prev
        last.prev.next = self.dummy
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummy.next.value

        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummy.prev.value
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()