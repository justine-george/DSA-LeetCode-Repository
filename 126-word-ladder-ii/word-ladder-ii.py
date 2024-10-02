class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Build adjacency list
        def getNeighbors(word):
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        yield newWord

        # BFS
        def bfs():
            level = 0
            queue = deque([(beginWord, [beginWord])])
            visited = set([beginWord])
            parents = defaultdict(set)
            found = False
            while queue and not found:
                level += 1
                level_size = len(queue)
                level_visited = set()
                
                for _ in range(level_size):
                    word, path = queue.popleft()
                    for neighbor in getNeighbors(word):
                        if neighbor == endWord:
                            found = True
                        if neighbor not in visited:
                            parents[neighbor].add(word)
                            if neighbor not in level_visited:
                                level_visited.add(neighbor)
                                queue.append((neighbor, path + [neighbor]))
                
                visited |= level_visited
            
            if not found:
                return []
            
            # Backtrack to find all paths
            def backtrack(word):
                return [[word]] if word == beginWord else [path + [word] for parent in parents[word] for path in backtrack(parent)]
            
            return backtrack(endWord)

        return bfs()