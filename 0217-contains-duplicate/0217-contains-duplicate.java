class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set visitedSet = new HashSet<Integer>();
        visitedSet.add(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            if (visitedSet.contains(nums[i]))
                return true;
            visitedSet.add(nums[i]);
        }
        return false;
    }
}