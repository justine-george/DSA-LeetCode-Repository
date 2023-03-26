class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >=0; j--) {
//                 // bottom right corner
//                 if (i == m - 1 && j == n - 1) dp[i][j] = 1;

//                 // value exist on right and below
//                 else if (i + 1 < m && j + 1 < n)
//                     dp[i][j] = dp[i][j + 1] + dp[i + 1][j];

//                 // value exist only on right
//                 else if (j + 1 < n)
//                     dp[i][j] = dp[i][j + 1];

//                 // value exist only on left
//                 else dp[i][j] = dp[i + 1][j];
                
                // more simpler approach
                // if edges
                if (i == m - 1 || j == n - 1) dp[i][j] = 1;
                else
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j];
            }
        }

        return dp[0][0];
    }
}