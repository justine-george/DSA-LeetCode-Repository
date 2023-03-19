class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer, Integer> firstOccurMap = new HashMap<>();
        HashMap<Integer, Integer> latestOccurMap = new HashMap<>();
        HashMap<Integer, Integer> countMap = new HashMap<>();
 
        int maxCount = 0;
        for (int i = 0; i < nums.length; i++) {
            if (!firstOccurMap.containsKey(nums[i]))
                firstOccurMap.put((nums[i]), i);
            countMap.put((nums[i]), countMap.getOrDefault(nums[i], 0) + 1);
            latestOccurMap.put((nums[i]), i);
            maxCount = Math.max(maxCount, countMap.get(nums[i]));
        }
        
        int minLen = Integer.MAX_VALUE;
        for (Map.Entry<Integer, Integer> e: countMap.entrySet()) {
            if (e.getValue() == maxCount) {
                minLen = Math.min(minLen, latestOccurMap.get(e.getKey()) - firstOccurMap.get(e.getKey()) + 1);
            }
        }
        return minLen;
        
    }
}