class Solution {
    public boolean carPooling(int[][] trips, int capacity) {

        // PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> (a - b));
        
        // Arrays.sort(trips, (a, b) -> (a[1] - b[1]));
        // int remainSeats = capacity;

        // for (int[] arr : trips) {

        //     int seats = arr[0];
        //     int from = arr[1];
        //     int to = arr[2];

        //     if (heap.isEmpty()) {
        //         remainSeats -= seats;
        //         heap.offer(to);
        //     }


        //     if (!heap.isEmpty()) {

        //         int lastTrip = heap.peek();
        //         if (lastTrip >= from) {
        //             if (remainSeats >= seats) {
        //                 remainSeats -= seats;
        //                 heap.poll();
        //                 heap.offer(to);
        //             }
        //             else {
        //                 return false;
        //             }
        //         } 
        //         else if (lastTrip <= from) {
        //             if (remainSeats >= seats) {
        //                 remainSeats -= seats;
        //                 // heap.poll();
        //                 heap.offer(to);
        //             }
        //             else {
        //                 return false;
        //             }
        //         }
        //     }
        // }
        // return true;



        Arrays.sort(trips, (a, b) -> Integer.compare(a[1], b[1]));

        // Min-heap based on drop-off point
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        int currentPassengers = 0;

        for (int[] trip : trips) {
            int numPassengers = trip[0];
            int from = trip[1];
            int to = trip[2];

            // Drop off all passengers before this trip starts
            while (!pq.isEmpty() && pq.peek()[0] <= from) {
                currentPassengers -= pq.poll()[1];
            }

            // Pick up new passengers
            currentPassengers += numPassengers;

            if (currentPassengers > capacity) {
                return false;
            }

            // Add new trip to heap
            pq.offer(new int[]{to, numPassengers});
        }

        return true;
    }
}