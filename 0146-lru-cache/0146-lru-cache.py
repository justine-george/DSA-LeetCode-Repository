class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # add to right
    def add(self, node):
        #           node
        # prev(mru)      next(dummy to mru)
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next
        
    # remove lru, from left
    def remove(self, node):    
        # prev  node  next
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        self.add(self.map[key])
        if len(self.map) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)