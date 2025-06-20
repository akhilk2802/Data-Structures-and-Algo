class Solution {
    public void wallsAndGates(int[][] rooms) {
        // '''
        // INF -> empty room
        // -1 -> obstacle / wall
        // 0 -> gate 

        // place all the gates in the queue

        // '''

        Queue<int[]> gates = new LinkedList<>();

        int m = rooms.length;
        int n = rooms[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    gates.offer(new int[] {i, j});
                }
            }
        }

        int INF = 2147483647;
        int[][] directions = new int[][]{
            {0, 1},
            {1, 0},
            {-1, 0},
            {0, -1}
        };
        
        while (!gates.isEmpty()) {
            int size = gates.size();

            for (int i = 0; i < size; i++) {
                int[] loc = gates.poll();
                int x = loc[0];
                int y = loc[1];

                for (int[] dir : directions){
                    int newX = x + dir[0];
                    int newY = y + dir[1];

                    if ( newX >= 0 && newX < m && newY >= 0 && newY < n && rooms[newX][newY] == INF){
                        rooms[newX][newY] = Math.min(rooms[x][y] + 1, rooms[newX][newY]);
                        gates.offer(new int[] {newX, newY});
                    }
                }

            }

        }
        System.out.println(Arrays.deepToString(rooms));
        // return rooms;

    }
}