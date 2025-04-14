class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move node to the tail (most recently used).
            self.remove(node)
            self.add(node)
            return node.val
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.cache[node_to_delete.key]

    def add(self, node: ListNode):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev