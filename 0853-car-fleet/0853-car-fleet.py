class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # visualize in a cartesian plane, speed is the slope, position is the y axis, and time is x axis.
        # make a pair. then sort and iterate in reverse
        # [
        #     (0, 1),
        #     (3, 3),
        #     (5, 1),
        #     (8, 4),
        #     (10, 2)
        # ]
        # T: O(nlogn)
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()
        st = []
        
        for p, s in pair[::-1]: # iterate in reverse
            # add to the stack only if p,s won't meet with top of the stack before target
            if not st or st and (target - p)/s > st[-1]:
                    st.append((target - p)/s)
        
        return len(st)