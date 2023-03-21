class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int count = 0;
        int[] remArr = new int[60];
        for (int t : time) {
            int r = t % 60;
            int complement = (60 - r) % 60; // the complement of r
            count += remArr[complement];
            remArr[r]++;
        }
        return count;
    }
}
