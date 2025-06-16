

import javax.xml.crypto.dsig.keyinfo.RetrievalMethod;

class Solution {
    public int findOccur(int[] nums, int target, Boolean leftBias){

        int left = 0;
        int right = nums.length - 1;
        int val = -1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1; 
            } else {
                if (leftBias) {
                    right = mid - 1;
                    val = mid;
                } else {
                    left = mid + 1;
                    val = mid;
                }
            }
        }
        
        return val;
    }

    public int[] searchRange(int[] nums, int target) {

        int[] result = new int[2];
        result[0] = findOccur(nums, target, true);
        result[1] = findOccur(nums, target, false);

        return result;

    }
}