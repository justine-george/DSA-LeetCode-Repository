class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        
        # Dummy nodes for head and tail of DLL
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove a node from DLL
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        # Add a node to the front (right after head)
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            # Move the accessed node to the front
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # If key exists, remove it
            self._remove(self.map[key])
        node = Node(key, value)
        # Add new node to the front
        self._add(node)
        self.map[key] = node
        # If the capacity is reached, remove the LRU item
        if len(self.map) > self.capacity:
            node_to_remove = self.tail.prev
            self._remove(node_to_remove)
            del self.map[node_to_remove.key]
