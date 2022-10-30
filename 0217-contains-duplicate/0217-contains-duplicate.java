class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        Set numSet = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            numSet.add(nums[i]);
            if (i != numSet.size() - 1)
                return true;
        }
        return false;
    }
}