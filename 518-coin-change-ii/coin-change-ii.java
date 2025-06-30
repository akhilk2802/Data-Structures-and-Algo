class Solution {
    public int change(int amount, int[] coins) {
        Map<String, Integer> memo = new HashMap<>();
        return dfs(0, 0, amount, coins, memo);
    }

    private int dfs(int index, int currentAmount, int target, int[] coins, Map<String, Integer> memo) {

        String key = index + "," + currentAmount;
        
        if (memo.containsKey(key)) return memo.get(key);
        if (currentAmount > target) return 0;
        if (currentAmount == target) return 1;
        if (index == coins.length) return 0;

        int include = dfs(index, currentAmount + coins[index], target, coins, memo);
        int skip = dfs(index + 1, currentAmount, target, coins, memo);

        memo.put(key, include + skip);
        return memo.get(key);
    }
}