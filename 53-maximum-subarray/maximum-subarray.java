class Solution {
    public int maxSubArray(int[] nums) {

        int max_sum = Integer.MIN_VALUE;
        int current_sum = 0;

        for (int i = 0; i < nums.length; i++) {
            current_sum = Math.max(nums[i], nums[i] + current_sum);
            max_sum = Math.max(current_sum, max_sum);
        }

        return max_sum;
        
    }
}