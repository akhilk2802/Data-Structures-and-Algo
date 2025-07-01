class Solution {
    public int maximumCandies(int[] candies, long k) {

        int low = 1;
        int high = 0;

        for (int candy : candies) {
            if (high < candy) {
                high = candy;
            }
        }
        int result = 0;

        while (low <= high) {

            int mid = (low + high) / 2;

            if (canDivide(mid, candies, k)) {
                result = mid;
                low = mid + 1;
            } else{
                high = mid - 1;
            }
        }
        return result;
    }

    public boolean canDivide(int mid, int[] candies, long k) {
        long total = 0;
        for (int candy : candies) {
            if (candy / mid > 0) {
                total += candy / mid;
            }
        }
        if (total >= k) {
            return true;
        }
        return false;
    }
}