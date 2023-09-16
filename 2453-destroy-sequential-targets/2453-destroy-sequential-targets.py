from collections import defaultdict

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mod_counts = defaultdict(int)
        mod_smallest = defaultdict(lambda: float('inf'))

        for num in nums:
            mod = num % space
            mod_counts[mod] += 1
            mod_smallest[mod] = min(mod_smallest[mod], num)

        # Find the modulus with maximum count
        max_count = max(mod_counts.values())
        max_count_mods = [mod for mod, count in mod_counts.items() if count == max_count]

        # Among the moduli with maximum count, find the one associated with the smallest number
        return min(mod_smallest[mod] for mod in max_count_mods)
