class Solution {
    public int maxSubArray(int[] nums) {
        int curr = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            
            curr = Math.max(num, curr + num);
            
            if (curr > max)
                max = curr;
        }
        return max;
    }
}