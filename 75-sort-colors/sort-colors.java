class Solution {
    public void sortColors(int[] nums) {

        int low = 0;
        int mid = 0;
        int high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {

                int temp = nums[mid];
                nums[mid] = nums[low];
                nums[low] = temp;

                low += 1;
                mid += 1;
            } else if (nums[mid] == 1) {
                mid += 1;
            } else {

                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                
                high -= 1;
            }
        }

        // for (int i = 1; i < nums.length; i++) {
        //     for (int j = 0; j  < i; j ++) {

        //         if (nums[i] < nums[j]) {
        //             int temp = nums[i];
        //             nums[i] = nums[j];
        //             nums[j] = temp;
        //         }
        //     }
        // }
    }
}