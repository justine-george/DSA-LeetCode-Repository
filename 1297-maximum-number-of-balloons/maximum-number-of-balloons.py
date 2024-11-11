class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_freq_map = Counter('balloon')
        text_freq_map = Counter(text)

        no_of_balloons = float('inf')
        for char, freq in balloon_freq_map.items():
            if char not in text_freq_map or text_freq_map[char] < balloon_freq_map[char]:
                return 0
            no_of_balloons = min(no_of_balloons, text_freq_map[char] // freq)
        
        return no_of_balloons