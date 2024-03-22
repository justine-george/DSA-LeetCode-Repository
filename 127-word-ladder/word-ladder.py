class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # make adjacency list
        adjlist = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                # for each position, replace with wild card char
                pattern = word[ : j] + '*' + word[j + 1 : ]
                adjlist[pattern].append(word)

        # bfs
        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            # go layer by layer
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                # get neighbors
                # first find all pattern this word falls into, then get from adjlist
                for j in range(len(word)):
                    pattern = word[ : j] + '*' + word[j + 1 : ]
                    for neighborWord in adjlist[pattern]:
                        if neighborWord not in visit:
                            visit.add(neighborWord)
                            q.append(neighborWord)

            res += 1

        return 0