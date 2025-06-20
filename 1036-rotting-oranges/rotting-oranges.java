class Solution {
    public int orangesRotting(int[][] grid) {


        int fresh = 0;
        Queue<int[]> rotten = new LinkedList<>();

        int m = grid.length;
        int n = grid[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2){
                    rotten.offer(new int[] {i, j});
                }
                if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }
        System.out.println("fresh -> " + fresh);

        if (fresh == 0){
            return 0;
        }

        int minutes = 0;
        int[][] directions = new int[][] {{0,1}, {1,0}, {-1,0}, {0,-1}};
        
        while (!rotten.isEmpty()){
            boolean rotted = false;
            int rottenQueueSize = rotten.size();

            for (int i = 0; i < rottenQueueSize; i++) {
                int[] loc = rotten.poll();
                int x = loc[0];
                int y = loc[1];

                for (int[] dir : directions){
                    int nx = x + dir[0];
                    int ny = y + dir[1];

                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1){
                        grid[nx][ny] = 2;
                        rotten.offer(new int[] {nx, ny});
                        fresh--;
                        rotted = true;
                    }
                }
            }
            if (rotted) {
                minutes++;
            }

        }
        return fresh == 0 ? minutes : -1;
    }
}