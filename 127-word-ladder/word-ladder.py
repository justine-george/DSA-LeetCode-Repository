class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # lowerAlphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        #build adjacency list, for every word, generate pattern.
        # then map: pattern -> words that fit that pattern
        graph = defaultdict(list)
        # {
        #     "*ot": [hot, dot, lot]
        # }
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                graph[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in visited and neighbor != word and neighbor in wordSet:
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1

        return 0
