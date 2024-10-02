class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        wordListSet = set(wordList)

        while q:
            word, count = q.popleft()

            # if word == endWord:
            #     return count

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]

                    if newWord == endWord and newWord in wordListSet:
                        return count + 1

                    if newWord not in visited and newWord != word and newWord in wordListSet:
                        q.append((newWord, count + 1))
                        visited.add(newWord)

        return 0
