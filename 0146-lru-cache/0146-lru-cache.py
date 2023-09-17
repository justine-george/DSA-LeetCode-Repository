from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        
        # new items added to the right
        # remove on get and add to right
        # left contains least recently used
        self.keyStack = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            # remove key frm keyStack and add to right
            # TODO
            self.keyStack.remove(key)
            self.keyStack.append(key)
            
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if len(self.keyStack) == self.capacity:
                deleteKey = self.keyStack.popleft()
                del self.map[deleteKey]
            self.map[key] = value
            self.keyStack.append(key)
        else:
            self.map[key] = value
            
            # remove key frm keyStack and add to right
            # TODO
            self.keyStack.remove(key)
            self.keyStack.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

