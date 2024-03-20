from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        G = defaultdict(list)
        for time, user, web in sorted(zip(timestamp, username, website)):
            G[user].append(web)
        
        scores = defaultdict(int)
        for user, websites in G.items():
            for pattern in set(combinations(websites, 3)):
                scores[pattern] += 1
            
        
        max_pattern, max_count = '', 0
        for pattern, count in scores.items():
            if (count > max_count) or (count == max_count and pattern < max_pattern):
                max_pattern = pattern
                max_count = count

        return max_pattern