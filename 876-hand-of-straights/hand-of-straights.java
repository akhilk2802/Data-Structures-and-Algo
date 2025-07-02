class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {

        int n = hand.length;
        if (n % groupSize != 0) return false;

        Map<Integer, Integer> map = new HashMap<>();

        for (int num : hand) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        Arrays.sort(hand);
        for (int i = 0; i < n; i++) {
            if (map.get(hand[i]) > 0) {
                for (int j = hand[i]; j < (hand[i] + groupSize); j++) {
                    if (map.getOrDefault(j, 0) < 1) return false;
                    map.put(j, map.get(j) - 1);

                }
            }
        }
        return true;
    }
}