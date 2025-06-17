class Solution {
    public int minMeetingRooms(int[][] intervals) {

        if (intervals.length == 0 || intervals.equals(null)) {
            return 0;
        }

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        PriorityQueue<Integer> min_heap = new PriorityQueue<>();

        for (int[] interval : intervals){
            int start = interval[0];
            int end = interval[1];

            if (min_heap.size() > 0 && min_heap.peek() <= start) {
                min_heap.poll();
            }

            min_heap.add(end);
        }

        return min_heap.size();

        // for (int[] interval : intervals){
        //     System.out.println(interval[0]);

        // }

        // return 0;
    }
}