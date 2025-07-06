class Solution {
    public int trap(int[] height) {

        int left = 0, right = height.length - 1;
        int maxLeft = height[left];
        int maxRight = height[right];
        int total = 0;

        while (left < right) {
            if (height[left] <= height[right]) {
                left++;
                if (height[left] > maxLeft) {
                    maxLeft = height[left];
                } else {
                    total += maxLeft - height[left];
                }
            } else {
                right--;
                if (height[right] > maxRight) {
                    maxRight = height[right];
                } else {
                    total += maxRight - height[right];
                }
            }
        }

        return total;
        
    }
}