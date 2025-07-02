class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {

        Map<Integer, Integer> freq_map = new HashMap<>();

        int n = nums.length;
        if (n % k != 0) return false;

        for (int num : nums) {
            freq_map.put(num, freq_map.getOrDefault(num, 0) + 1);
        }

        Arrays.sort(nums);
        for (int num : nums) {
            if (freq_map.get(num) > 0) {
                for (int i = num; i < (num + k); i++) {
                    if (freq_map.getOrDefault(i, 0) == 0) return false;
                    freq_map.put(i, freq_map.get(i) - 1);
                }
            }
        }
        return true;
    }
}