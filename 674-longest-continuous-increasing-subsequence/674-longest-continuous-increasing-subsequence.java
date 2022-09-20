// class Solution {
//     public int findLengthOfLCIS(int[] nums) {
//         int[] cisLength = new int[nums.length];
        
//         // initialize 1 to every elements of cisLength
//         for (int i = 0; i < cisLength.length; i++) {
//             cisLength[i] = 1;
//         }
        
//         // find length of continuous increasing subsequence from each index
//         for (int i = 0; i < nums.length; i++) {
//             for (int j = i; j < nums.length - 1; j++) {
//                 if (nums[j] < nums[j+1])
//                     cisLength[i]++;
//                 else
//                     break;
//             }
//         }
        
//         // find max length of LCIS and return
//         int max = -1;
//         for (int a: cisLength) {
//             if (a > max)
//                 max = a;
//         }
//         return max;
//     }
// }

class Solution {
    public int findLengthOfLCIS(int[] nums) {
        
        List<List<Integer>> subsequenceList = new ArrayList<>();
        
        // store increasing subsequences in a list of lists
        List<Integer> subsequence = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            subsequence.add(nums[i]);
            if (i == nums.length - 1) {
                subsequenceList.add(subsequence);
                break;
            }
            if (nums[i] < nums[i+1]) {
                // continue
            } else {
                subsequenceList.add(subsequence);
                subsequence = new ArrayList<>();
            }
        }
        
        // find max lengtha among lists
        int max = -1;
        for (List<Integer> a: subsequenceList) {
            if (a.size() > max)
                max = a.size();
        }
        return max;
    }
}