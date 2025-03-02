class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, newNode):
        previousNode = self.tail.prev
        previousNode.next = newNode
        newNode.prev = previousNode
        newNode.next = self.tail
        self.tail.prev = newNode

    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key not in self.dict.keys():
            return -1

        node = self.dict[key]
        self.remove(node)
        self.add(node)
        
        return self.dict[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            oldNode = self.dict[key]
            self.remove(oldNode)
        
        newNode = ListNode(key,value)
        self.dict[key] = newNode
        self.add(newNode)
        
        if len(self.dict) > self.capacity:
            removeNode = self.head.next
            self.remove(removeNode)
            del self.dict[removeNode.key]
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)