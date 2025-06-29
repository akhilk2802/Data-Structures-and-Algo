class Solution {
    public int maxSubArray(int[] nums) {
        
        int max_sum = Integer.MIN_VALUE;
        int curr_sum = 0;

        for (int i = 0; i< nums.length; i++) {
            curr_sum = Math.max(nums[i], nums[i] + curr_sum);
            max_sum = Math.max(max_sum, curr_sum);
        }
        return max_sum;
    }
}