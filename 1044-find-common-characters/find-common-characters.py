class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        
        prevWord = words[0]
        for i in range(1, len(words)):
            res = []
            print(prevWord)
            print(words[i])
            print("--")
            count_prev = Counter(prevWord)
            count_cur = Counter(words[i])

            for key in count_cur:
                if key in count_prev:
                    for i in range(min(count_cur[key], count_prev[key])):
                        res.append(key)

            prevWord = "".join(res)
        
        return prevWord