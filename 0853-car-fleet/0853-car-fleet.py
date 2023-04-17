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
        # T: O(nlogn)\
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()
        st = []
        
        for p, s in pair[::-1]:
            # if p,s meet with top of the stack before target, don't add it to the stack
            if st:
                if (target - p)/s > (target - st[-1][0])/(st[-1][1]):
                    st.append((p, s))
            else:
                st.append((p, s))
            
        
        
        
        
        return len(st)