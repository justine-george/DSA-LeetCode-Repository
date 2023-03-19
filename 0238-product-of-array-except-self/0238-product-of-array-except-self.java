class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        
        ans[0] = 1;
        int pre = 1;
        // pre
        for (int i = 1; i < nums.length; i++) {
            pre = pre * nums[i - 1];
            ans[i] = pre;
        }
        // post
        int post = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            post = post * nums[i + 1];
            ans[i] = post * ans[i];
        }
        return ans;
    }
}