class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # {key: Node()}
        self.map = {}
        # dummy nodes
        # left.next is the least recently used
        # right.prev is the most recently used, right.prev points to the latest node we add.
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left


    def add(self, node):
        # add just before self.right
        l, r = self.right.prev, self.right
        
        # add newNode between l and r
        node.prev = l
        node.next = r
        l.next = r.prev = node

    def remove(self, node):
        l, r = node.prev, node.next
        l.next = r
        r.prev = l

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.remove(self.map[key])
        self.add(self.map[key])
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        self.map[key] = Node(key, value)
        self.add(self.map[key])

        if len(self.map) > self.capacity:
            # remove the least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)