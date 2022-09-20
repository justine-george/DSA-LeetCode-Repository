// Solution 1
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

// Solution 2
// class Solution {
//     public int findLengthOfLCIS(int[] nums) {
        
//         List<List<Integer>> subsequenceList = new ArrayList<>();
        
//         // store increasing subsequences in a list of lists
//         List<Integer> subsequence = new ArrayList<>();
//         for (int i = 0; i < nums.length; i++) {
//             subsequence.add(nums[i]);
//             if (i == nums.length - 1) {
//                 subsequenceList.add(subsequence);
//                 break;
//             }
//             if (nums[i] < nums[i+1]) {
//                 // continue
//             } else {
//                 subsequenceList.add(subsequence);
//                 subsequence = new ArrayList<>();
//             }
//         }
        
//         for (List<Integer> aList: subsequenceList) {
//             for (Integer a: aList) {
//                 System.out.print("" + a);
//             }
//             System.out.print("\n");
//         }
        
//         // find max length among lists
//         int max = -1;
//         for (List<Integer> a: subsequenceList) {
//             if (a.size() > max)
//                 max = a.size();
//         }
//         return max;
//     }
// }

class Solution {
    public int findLengthOfLCIS(int[] nums) {
        
        int answer = 1, counter = 1;
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] < nums[i]) {
                counter++;
                answer = Math.max(answer, counter);
            } else {
                counter = 1;
            }
        }
        
        return answer;
    }
}