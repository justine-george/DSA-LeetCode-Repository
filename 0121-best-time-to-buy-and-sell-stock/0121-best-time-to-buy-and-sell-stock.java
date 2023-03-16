class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0, buyPrice = prices[0];
        for (int currPrice: prices) {
            buyPrice = Math.min(buyPrice, currPrice);
            maxProfit = Math.max(maxProfit, currPrice - buyPrice);
        }
        return maxProfit;
    }
}
