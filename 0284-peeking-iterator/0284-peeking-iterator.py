# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.i = 0
        self.map = {}

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.i in self.map:
            return self.map[self.i]
        self.map[self.i] = self.it.next()
        return self.map[self.i]

    def next(self):
        """
        :rtype: int
        """
        if self.i in self.map:
            val = self.map[self.i]
            self.i += 1
            return val
        val = self.it.next()
        self.i += 1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i in self.map:
            return True
        return self.it.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].