class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer, Integer> firstOccurMap = new HashMap<>();
        HashMap<Integer, Integer> latestOccurMap = new HashMap<>();
        HashMap<Integer, Integer> countMap = new HashMap<>();
 
        for (int i = 0; i < nums.length; i++) {
            if (!firstOccurMap.containsKey(nums[i])) {
                firstOccurMap.put((nums[i]), i);
                countMap.put((nums[i]), 1);
            } else {
                countMap.put((nums[i]), countMap.get(nums[i]) + 1);
            }
            latestOccurMap.put((nums[i]), i);
        }
        
        int maxCount = 0;
        for (Map.Entry<Integer, Integer> e: countMap.entrySet()) {
            int key = e.getKey();
            int val = e.getValue();
            maxCount = Math.max(maxCount, val);
        }
        
        int minLen = Integer.MAX_VALUE;
        for (Map.Entry<Integer, Integer> e: countMap.entrySet()) {
            int key = e.getKey();
            int val = e.getValue();
            if (val == maxCount) {
                minLen = Math.min(minLen, latestOccurMap.get(key) - firstOccurMap.get(key) + 1);
            }
        }
        return minLen;
    }
}