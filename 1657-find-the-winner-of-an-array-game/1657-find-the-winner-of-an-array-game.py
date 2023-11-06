class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
            
        current_winner = arr[0]
        win_count = 0

        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                win_count += 1
            else:
                current_winner = arr[i]
                win_count = 1
            
            if win_count == k:
                return current_winner
        
        return current_winner