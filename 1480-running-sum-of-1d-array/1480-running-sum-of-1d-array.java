// class Solution {
//     public int[] runningSum(int[] nums) {
//         int[] runSum = new int[nums.length];
        
//         runSum[0] = nums[0];
//         for (int i = 1; i < nums.length; i++) {
//             runSum[i] = nums[i] + runSum[i-1];
//         }
        
//         return runSum;
//     }
// }

class Solution {
    public int[] runningSum(int[] nums) {
        
        for (int i = 1; i < nums.length; i++) {
            nums[i] = nums[i] + nums[i-1];
        }
        
        return nums;
    }
}