from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        def generate_combinations(list, k):
            res = []

            def combine(start, curr_arr):
                if len(curr_arr) == k:
                    res.append(tuple(curr_arr))
                    return
                    
                for i in range(start, len(list)):
                    curr_arr.append(list[i])
                    combine(i + 1, curr_arr)
                    curr_arr.pop()

            combine(0, [])
            return res
        
        # def generate_permutations(list, k):
        #     res = []
            
        #     def permute(curr_arr):
        #         if len(curr_arr) == k:
        #             res.append(tuple(curr_arr))
        #             return
                
        #         for i in range(len(list)):
        #             if list[i] in curr_arr:
        #                 continue
        #             curr_arr.append(list[i])
        #             permute(curr_arr)
        #             curr_arr.pop()

        #     permute([])
        #     return res
        
        G = defaultdict(list)
        for time, user, web in sorted(zip(timestamp, username, website)):
            G[user].append(web)
        
        scores = defaultdict(int)
        for user, websites in G.items():
            # for pattern in set(combinations(websites, 3)):
            #     scores[pattern] += 1
            for pattern in set(generate_combinations(websites, 3)):
                scores[pattern] += 1
            
        max_pattern, max_count = '', 0
        for pattern, count in scores.items():
            # for same count, tie break using lexicographic order
            if (count > max_count) or (count == max_count and pattern < max_pattern):
                max_pattern = pattern
                max_count = count

        return max_pattern