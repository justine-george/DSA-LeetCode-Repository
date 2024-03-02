# from sortedcontainers import SortedDict

class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        curNode = self.root
        if path != "/":
            pathItems = path.split("/")[1:]
            for pathItem in pathItems:
                curNode = curNode.children.get(pathItem)
                # check if its a file path
                if curNode and curNode.content is not None:
                    return [pathItem]
        return sorted(list(curNode.children.keys()))

    def mkdir(self, path: str) -> None:
        curNode = self.root
        pathItems = path.split("/")[1:]
        for pathItem in pathItems:
            if pathItem not in curNode.children:
                curNode.children[pathItem] = TrieNode()
            curNode = curNode.children.get(pathItem)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curNode = self.root
        pathItems = filePath.split("/")[1:]
        for pathItem in pathItems:
            if pathItem not in curNode.children:
                curNode.children[pathItem] = TrieNode()
            curNode = curNode.children.get(pathItem)
        
        curNode.content = (curNode.content or '') + content

    def readContentFromFile(self, filePath: str) -> str:
        curNode = self.root
        pathItems = filePath.split("/")[1:]
        for pathItem in pathItems:
            curNode = curNode.children.get(pathItem)
        return curNode.content

class TrieNode:
    def __init__(self):
        self.content = None
        self.children = {}

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)