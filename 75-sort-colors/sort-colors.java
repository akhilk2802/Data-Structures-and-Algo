class Solution {
    public void sortColors(int[] nums) {

        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j  < i; j ++) {

                if (nums[i] < nums[j]) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
    }
}