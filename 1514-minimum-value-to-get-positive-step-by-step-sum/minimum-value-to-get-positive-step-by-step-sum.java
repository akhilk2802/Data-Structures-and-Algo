class Solution {
    public int minStartValue(int[] nums) {

        int sum = 0;
        int minPrefixSum = 0;

        for (int num : nums){
            sum += num;
            minPrefixSum = Math.min(minPrefixSum, sum);
        }

        return 1 - minPrefixSum;
        
    }
}