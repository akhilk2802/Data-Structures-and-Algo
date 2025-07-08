import java.util.*;

class Solution {
    public int maxProfit(int k, int[] prices) {
        // Edge cases
        if (k == 0 || prices.length < 2) return 0;
        // If k is large enough, it’s just as if unlimited transactions
        if (k >= prices.length / 2) return quickSolve(prices);

        Map<String, Integer> memo = new HashMap<>();
        return dfs(prices, 0, true, k, memo);
    }

    private int dfs(int[] prices, int day, boolean canBuy, int transactionsRemaining, Map<String, Integer> memo) {
        // Base case: no days left or no transactions left
        if (day == prices.length || transactionsRemaining == 0) {
            return 0;
        }

        // Build a unique key for this state
        String key = day + "|" + canBuy + "|" + transactionsRemaining;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int doNothing = dfs(prices, day + 1, canBuy, transactionsRemaining, memo);
        int doAction;
        if (canBuy) {
            // Option 1: buy stock today (spend prices[day])
            doAction = -prices[day] + dfs(prices, day + 1, false, transactionsRemaining, memo);
        } else {
            // Option 2: sell stock today (earn prices[day]), consumes one transaction
            doAction = prices[day] + dfs(prices, day + 1, true, transactionsRemaining - 1, memo);
        }

        int best = Math.max(doNothing, doAction);
        memo.put(key, best);
        return best;
    }

    // If unlimited transactions are allowed, just sum all positive rises
    private int quickSolve(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) profit += diff;
        }
        return profit;
    }
}