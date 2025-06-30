class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        Map<String, Integer> memo = new HashMap<>();
        return dfs(nums, 0, 0, target, memo);
    }

    private int dfs(int[] nums, int index, int currentSum, int target, Map<String, Integer> memo) {
        String key = index + "," + currentSum;

        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        if (index == nums.length) {
            return currentSum == target ? 1 : 0;
        }

        int positive = dfs(nums, index + 1, currentSum + nums[index], target, memo);
        int negative = dfs(nums, index + 1, currentSum - nums[index], target, memo);

        memo.put(key, positive + negative);
        return memo.get(key);
    }
}