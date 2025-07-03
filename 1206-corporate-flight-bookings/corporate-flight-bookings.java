class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {

        /*
        [0,0,0,0,0]
        */

        int[] diffArray = new int[n + 1];

        for (int[] arr : bookings) {
            
            int first = arr[0];
            int last =  arr[1];
            int seats = arr[2];

            diffArray[first - 1] += seats;
            diffArray[last] -= seats;
        }

        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            if (i == 0) {
                result[i] = 0 + diffArray[i];
            } else {
                result[i] = result[i-1] + diffArray[i];
            }
        }
        return result;
        
    }
}