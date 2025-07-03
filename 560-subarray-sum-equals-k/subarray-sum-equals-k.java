class Solution {
    public int subarraySum(int[] nums, int k) {

        int[] prefixSumArray = new int[nums.length];

        int prefixSum = 0;
        for (int i = 0; i < nums.length; i++) {
            prefixSum += nums[i];
            prefixSumArray[i] = prefixSum;
        }
        int count = 0;
        
        for (int i = 0; i < nums.length; i++) {

            if (prefixSumArray[i] == k) {
                count++;
            }

            for (int j = 0; j < i; j++) {
                if (prefixSumArray[i] - prefixSumArray[j] == k) {
                    count++;
                }
                
            }
        }
        return count;
    }
}