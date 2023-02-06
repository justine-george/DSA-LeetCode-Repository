class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        // Arrays.fill(answer, 1);
        answer[0] = 1;
        // leftside values
        for (int i = 1; i < nums.length; i++) {
            answer[i] = nums[i-1] * answer[i-1];
        }
        // rightside values
        int mul = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            mul *= nums[i+1];
            answer[i] = mul * answer[i];
        }
        return answer;
    }
}

