# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.generator = self.intGenerator(nestedList)
        self.next_int = next(self.generator, None)
    
    def intGenerator(self, nestedList):
        for nested in nestedList:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                yield from self.intGenerator(nested.getList())
    
    def next(self) -> int:
        res = self.next_int
        self.next_int = next(self.generator, None)
        return res
    
    def hasNext(self) -> bool:
        return self.next_int is not None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())