class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set visitedSet = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (visitedSet.contains(nums[i]))
                return true;
            visitedSet.add(nums[i]);
        }
        return false;
    }
}