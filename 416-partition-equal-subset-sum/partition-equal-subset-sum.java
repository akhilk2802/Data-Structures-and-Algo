class Solution {
    public boolean canPartition(int[] nums) {

        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        if (sum % 2 != 0) {
            return false;
        }

        int target = sum / 2;
        Set<Integer> dp = new HashSet<>();
        dp.add(0);

        for (int i = 0; i < nums.length; i++) {
            Set<Integer> nextDP = new HashSet<>(dp);

            if (nums[i] == target) {
                return true;
            }
            for (int j : dp ) {
                if (j + nums[i] == target) {
                    return true;
                }
                nextDP.add(nums[i]);
                nextDP.add(nums[i] + j);
            }
            dp = nextDP;
        }

        return false;
    }
}