class Solution {
    public boolean canJump(int[] nums) {
        int farthest = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i > farthest) {
                return false;
            }
            farthest = Math.max(farthest, i + nums[i]);
        }

        return true;
    }
    // public boolean canJump(int[] nums) {

    //     if (nums[0] <= 0) {
    //         return false;
    //     }

    //     int jumpsRemaining = nums[0];
    //     int i = 1;
        
    //     while (i < nums.length) {
            
    //         if (jumpsRemaining < 0) {
    //             return false;
    //         }
    //         else if (jumpsRemaining < nums[i]) {
    //             jumpsRemaining = nums[i];
    //         }
    //         jumpsRemaining--;
    //         i++;
    //     }
    //     return true;  
    // }
}