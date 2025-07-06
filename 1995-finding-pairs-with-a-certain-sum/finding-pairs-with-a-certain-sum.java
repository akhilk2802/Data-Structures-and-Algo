class FindSumPairs {

    int[] nums1;
    int[] nums2;
    Map<Integer, Integer> freq2; // freq map for nums2

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.freq2 = new HashMap<>();

        for (int num : nums2) {
            freq2.put(num, freq2.getOrDefault(num, 0) + 1);
        }
    }

    public void add(int index, int val) {
        int oldVal = nums2[index];
        int newVal = oldVal + val;

        // Update freq map
        freq2.put(oldVal, freq2.get(oldVal) - 1);
        if (freq2.get(oldVal) == 0) {
            freq2.remove(oldVal);
        }

        freq2.put(newVal, freq2.getOrDefault(newVal, 0) + 1);

        nums2[index] = newVal;
    }

    public int count(int tot) {
        int count = 0;
        for (int num : nums1) {
            int complement = tot - num;
            count += freq2.getOrDefault(complement, 0);
        }
        return count;
    }
}