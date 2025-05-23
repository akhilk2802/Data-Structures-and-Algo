class LinkedList:
    def __init__(self, value, nextNode = None):
        self.val = value
        self.next = nextNode

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.count = 0
        self.head = None
        self.tail = None
        

    def enQueue(self, value: int) -> bool:
        if self.count >= self.capacity:
            return False

        if self.count == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = self.head
        else:
            new_node = ListNode(value)
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return True
        

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True
        

    def Front(self) -> int:

        if self.count == 0:
            return -1
        return self.head.val
        

    def Rear(self) -> int:

        if self.count == 0:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:

        return self.count == 0
        

    def isFull(self) -> bool:

        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()