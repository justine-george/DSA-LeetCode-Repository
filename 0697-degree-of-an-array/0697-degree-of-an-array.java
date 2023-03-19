class Solution {
    public int findShortestSubArray(int[] nums) {
//         HashMap<Integer, Integer> firstOccurMap = new HashMap<>();
//         HashMap<Integer, Integer> latestOccurMap = new HashMap<>();
//         HashMap<Integer, Integer> countMap = new HashMap<>();
 
//         int maxCount = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (!firstOccurMap.containsKey(nums[i])) {
//                 firstOccurMap.put((nums[i]), i);
//                 countMap.put((nums[i]), 1);
//             } else {
//                 countMap.put((nums[i]), countMap.get(nums[i]) + 1);
//             }
//             latestOccurMap.put((nums[i]), i);
//             maxCount = Math.max(maxCount, countMap.get(nums[i]));
//         }
        
//         int minLen = Integer.MAX_VALUE;
//         for (Map.Entry<Integer, Integer> e: countMap.entrySet()) {
//             int key = e.getKey();
//             int val = e.getValue();
//             if (val == maxCount) {
//                 minLen = Math.min(minLen, latestOccurMap.get(key) - firstOccurMap.get(key) + 1);
//             }
//         }
//         return minLen;
        
        
        HashMap<Integer, Integer> firstOccurMap = new HashMap<>();
        HashMap<Integer, Integer> countMap = new HashMap<>();
        int maxCount = 0;
        int minLen = Integer.MAX_VALUE;

        for (int i = 0; i < nums.length; i++) {
            if (!firstOccurMap.containsKey(nums[i])) {
                firstOccurMap.put(nums[i], i);
                countMap.put(nums[i], 1);
            } else {
                countMap.put(nums[i], countMap.get(nums[i]) + 1);
            }
            int count = countMap.get(nums[i]);
            if (count > maxCount) {
                maxCount = count;
                minLen = i - firstOccurMap.get(nums[i]) + 1;
            } else if (count == maxCount) {
                minLen = Math.min(minLen, i - firstOccurMap.get(nums[i]) + 1);
            }
        }

        return minLen;
    }
}