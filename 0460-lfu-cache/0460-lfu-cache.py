class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}

    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = Node(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node
        
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            prev, next = node.prev, node.next
            next.prev = prev
            prev.next = next
            # self.map.pop(val)
            del self.map[val]
    
    def popLeft(self):
        res = self.left.next.val
        self.pop(res)
        return res
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCount = 0
        self.valMap = {} # Map key -> val
        
        # stores how many times a key has been used
        self.countMap = collections.defaultdict(int) # Map key -> count
        
        # Map count of key -> linkedlist
        self.listMap = collections.defaultdict(LinkedList)

    def counter(self, key):
        count = self.countMap[key]
        self.countMap[key] += 1
        
        self.listMap[count].pop(key)
        self.listMap[count + 1].pushRight(key)
        
        if count == self.lfuCount and self.listMap[count].length() == 0:
            self.lfuCount += 1
        
    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCount].popLeft()
            # self.valMap.pop(res)
            del self.valMap[res]
            self.countMap.pop(res)
        
        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.lfuCount, self.countMap[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)