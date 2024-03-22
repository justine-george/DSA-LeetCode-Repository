class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        
        n = len(wordList[0])

        adj_list = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + '*' + word[i+1:]
                adj_list[pattern].append(word)

        res = 1
        q = collections.deque([beginWord])
        visit = set([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(n):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neighborWord in adj_list[pattern]:
                        if neighborWord not in visit:
                            visit.add(neighborWord)
                            q.append(neighborWord)

            res += 1
        
        return 0