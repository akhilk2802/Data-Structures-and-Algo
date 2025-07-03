class Solution {
    public int findDuplicate(int[] nums) {

        int fast = nums[0];
        int slow = nums[0];

        boolean test = true;

        while (test) {
            slow = nums[slow];
            fast = nums[nums[fast]];

            if (fast == slow) {
                test = false;
                break;
            }
        }

        slow = nums[0];
        
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }

        return slow;

        // Set<Integer> seen = new HashSet<>();

        // for (int num : nums) {
        //     if (seen.contains(num)) {
        //         return num;
        //     }
        //     seen.add(num);
        // }
        // return -1;
    }
}