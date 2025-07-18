class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        int l = s.length();
        boolean[] dp = new boolean[l + 1];

        dp[0] = true;

        Set<String> wordSet = new HashSet<>(wordDict);

        for (int i = 1; i < s.length() + 1; i++ ){
            for (int j = 0; j < i; j++ ){
                if (dp[j] && wordSet.contains(s.substring(j, i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[l];
    }
}