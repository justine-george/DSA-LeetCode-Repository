class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0, currentWealth = 0;
        for (int i = 0; i < accounts.length; i++) {
            currentWealth = 0;
            for (int j = 0; j < accounts[0].length; j++) {
                currentWealth += accounts[i][j];
            }
            if (currentWealth > maxWealth )
                maxWealth = currentWealth;
        }
        return maxWealth;
    }
}