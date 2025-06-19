class Solution {
    public int lastStoneWeight(int[] stones) {
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();

        for (int stone : stones) {
            maxHeap.offer(-stone);
        }


        while (maxHeap.size() >= 2) {

            int stone1 = -maxHeap.poll();
            int stone2 = -maxHeap.poll();

            if (stone1 == stone2) {
                continue;
            }

            if (stone1 > stone2) {
                maxHeap.offer(-(stone1 - stone2));
            } else {
                maxHeap.offer(-(stone2 - stone1));
            }
        }

        if (maxHeap.size() == 1) {
            return -maxHeap.peek();
        }

        return 0;
    }
}