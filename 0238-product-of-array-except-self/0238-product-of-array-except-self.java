class Solution {
    public int[] productExceptSelf(int[] nums) {
        int mul = 1, zeroIndex = -1, zeroCount = 0;
        int[] answer = new int[nums.length];
        // find number of zeroes
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zeroIndex = i;
                zeroCount++;
            }
        }
        // case 0: two or more zeros
        if (zeroCount >= 2) {
            return new int[nums.length];
        }
        // calculate product of array
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
               mul *= nums[i];
            }
        }
        // case 1: one zero
        if (zeroIndex != -1) {
            answer[zeroIndex] = mul;
        } else { // case 2: no zeroes
           for (int i = 0; i < nums.length; i++) {
               answer[i] = mul / nums[i];
           }
        }
        return answer;
    }
}

