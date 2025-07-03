class Solution {
    public int[] getModifiedArray(int length, int[][] updates) {

        /*
        length ->
        updates -> [StartIdx, EndIdx, inc]

        arr = [0] * length

        [0,0,0,0,0]
        [0,2,2,2,0]
        [0,2,5,5,3]
        [-2,0,3,5,3]
        */

        int[] arr = new int[length];

        for (int i = 0; i < updates.length; i++) {
            int[] interval = updates[i];
            int start = interval[0];
            int end = interval[1];
            int inc = interval[2];

            for (int j = start; j <= end; j++ ) {
                arr[j] += inc;
            }
        }
        return arr;
    }
}