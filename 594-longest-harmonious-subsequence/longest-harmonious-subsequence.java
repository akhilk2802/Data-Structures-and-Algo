class Solution {
    public int findLHS(int[] nums) {

        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        int maxVal = 0;

        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            if (freqMap.containsKey(val + 1)) {
                maxVal = Math.max(maxVal, freqMap.get(val) + freqMap.get(val + 1));
            }
            if (freqMap.containsKey(val - 1)) {
                maxVal = Math.max(maxVal, freqMap.get(val) + freqMap.get(val - 1));
            }
        }
        return maxVal;
    }
}