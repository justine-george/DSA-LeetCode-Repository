class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # floyd-warshall, all-pairs shortest distance
        dist = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for i in range(len(original)):
            dist[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = min(cost[i], dist[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        cost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                if dist[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == float('inf'):
                    return -1
                cost += dist[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]

        return cost