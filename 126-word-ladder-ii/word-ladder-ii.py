class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        lowerLetters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        # Build adjacency list
        def getNeighbors(word):
            for i in range(len(word)):
                for c in lowerLetters:
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        yield newWord

        # BFS
        def bfs():
            level = 0
            queue = deque([beginWord])
            visited = set([beginWord])
            parents = defaultdict(set)
            found = False
            while queue and not found:
                level += 1
                level_size = len(queue)
                level_visited = set()
                
                for _ in range(level_size):
                    word = queue.popleft()
                    for neighbor in getNeighbors(word):
                        if neighbor == endWord:
                            found = True
                        if neighbor not in visited:
                            parents[neighbor].add(word)
                            if neighbor not in level_visited:
                                level_visited.add(neighbor)
                                queue.append(neighbor)
                
                visited |= level_visited
            
            if not found:
                return []
            
            # Backtrack to find all paths
            def backtrack(word):
                if word == beginWord:
                    return [[word]]
                
                all_paths = []
                for parent in parents[word]:
                    parent_paths = backtrack(parent)
                    for path in parent_paths:
                        all_paths.append(path + [word])
                return all_paths

            return backtrack(endWord)

        return bfs()
