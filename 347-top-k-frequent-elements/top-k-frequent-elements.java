class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a,b) -> (a.getValue() - b.getValue()));

        for (Map.Entry<Integer, Integer> me : freqMap.entrySet()){
            
            pq.add(me);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        
        int[] result = new int[k];
        int i = 0;
        while (!pq.isEmpty()) {
            result[i++] = pq.poll().getKey();
        }
        return result;
    }
}