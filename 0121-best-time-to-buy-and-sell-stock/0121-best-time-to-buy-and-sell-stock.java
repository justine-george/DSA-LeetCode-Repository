class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0, bP = prices[0];
        for (int p: prices) {
            if (p < bP)
                bP = p;
            if (maxP < p - bP)
                maxP = p - bP;
        }
        return maxP;
    }
}
