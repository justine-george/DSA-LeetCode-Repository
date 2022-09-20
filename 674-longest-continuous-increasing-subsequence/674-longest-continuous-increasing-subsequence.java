class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int[] cisLength = new int[nums.length];
        
        // initialize 1 to every elements of cisLength
        for (int i = 0; i < cisLength.length; i++) {
            cisLength[i] = 1;
        }
        
        // find length of continuous increasing subsequence from each index
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j - 1] < nums[j])
                    cisLength[i]++;
                else
                    break;
            }
        }
        
        // find max length of LCIS and return
        int max = -1;
        for (int a: cisLength) {
            if (a > max)
                max = a;
        }
        return max;
    }
}