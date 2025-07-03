class Solution {
    public int[] findErrorNums(int[] nums) {


        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int dup = -1, miss = 0;

        for (int i = 1; i < nums.length + 1; i++) {
            
            if (map.containsKey(i)) {
                if (map.get(i) == 2){
                    dup = i;
                }
            } else {
                miss = i;
            }
        }

        return new int[] {dup, miss};
        
    }
}