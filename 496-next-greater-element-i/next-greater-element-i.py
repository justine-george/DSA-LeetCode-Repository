class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        # Optimal, using monotonic decreasing stack
        # T: O(m + n), S: O(m)
        nums1Index = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1) # m

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                index = nums1Index[val]
                res[index] = cur
            
            if cur in nums1Index:
                stack.append(cur)
        
        return res

        # T: O(m.n), S: O(m)
        # nums1Index = {n: i for i, n in enumerate(nums1)}
        # res = [-1] * len(nums1) # m

        # for i in range(len(nums2)): # n
        #     if nums2[i] not in nums1Index:
        #         continue
        #     for j in range(i + 1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = nums1Index[nums2[i]]
        #             res[idx] = nums2[j]
        #             break
        
        # return res