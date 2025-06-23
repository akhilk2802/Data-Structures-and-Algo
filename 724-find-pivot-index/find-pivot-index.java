class Solution {
    public int pivotIndex(int[] nums) {

        int[] preSum = new int[nums.length];
        preSum[0] = nums[0];
        int[] sufSum = new int[nums.length];

        for (int i = 1; i < nums.length; i++) {
            preSum[i] = preSum[i-1] + nums[i];
        }

        sufSum[nums.length - 1] = nums[nums.length - 1];

        for (int j = nums.length - 2 ; j >= 0; j--) {
            sufSum[j] = sufSum[j + 1] + nums[j];
        }

        int i = 0;
        while (i < nums.length) {
            if (preSum[i] == sufSum[i]) {
                return i;
            }
            i++;
        }
        return -1;
    }
}