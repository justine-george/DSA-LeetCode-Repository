class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a pair of position and speed, sort the pairs, and iterate through them in reverse order
        # [(0, 1),(3, 3),(5, 1),(8, 4),(10, 2)]
        # T: O(nlogn)
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()
        st = [] # stack stores the time taken to reach the target
        
        for p, s in pair[::-1]: # iterate in reverse order
            # Add the pair to the stack only if it won't meet the top of the stack before reaching the target
            # A single check is sufficient, as there is no need to check values deeper in the stack since they have already been checked (the reason we iterate in reverse order)
            if not st or st and (target - p)/s > st[-1]: # time taken for the preceding car is longer than the one in front => they won't meet.
                    st.append((target - p)/s)
        return len(st)
    
    
        # slightly different code, same method
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        st = []
        
        for p, s in pair:
            st.append((target - p)/s)
            if len(st) >= 2 and st[-1] <= st[-2]: # top of the stack would be the car just behind st[-2]. If the car behind takes less or equal time than the car in the front to reach the target, then it is a fleet. so delete the faster car at the back from the stack,. ie pop.
                st.pop()
        return len(st)
                