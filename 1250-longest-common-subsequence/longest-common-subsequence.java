class Solution {
    public int longestCommonSubsequence(String text1, String text2) {

        int m = text1.length();
        int n = text2.length();

        String result = "";

        int[][] dp = new int[m + 1][n + 1];

        // for (int i = 1; i <= m; i++) {
        //     for (int j = 1; j <= n; j++) {
        //         if (text1.charAt(i - 1) == text2.charAt( j - 1)) {
        //             dp[i][j] = 1 + dp[i - 1][j - 1];
        //             result += text1.charAt(i - 1);
        //         } else {
        //             dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        //         }
        //     }
        // }
        // System.out.println("result -> " + result);
        // return dp[m][n];

        // int[][] dp = new int[m + 1][n + 1];

        for (int i = m - 1; i > -1; i--) {
            for (int j = n - 1; j > -1; j--) {
                if (text1.charAt(i) == (text2.charAt(j))) {
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                    // result += text1.charAt(i);
                } else {
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j+1]);
                }
            }
        }
        // System.out.println("result -> " + result);
        return dp[0][0];


        
    }
}