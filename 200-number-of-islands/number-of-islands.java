class Solution {
    public void dfs(char[][] grid, boolean[][] visited, int i, int j) {
        int m = grid.length;
        int n = grid[0].length;

        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0' || visited[i][j]) {
            return;
        }
        
        visited[i][j] = true;

        int[][] directions = new int[][]{
            {0, 1},
            {1, 0},
            {-1, 0},
            {0, -1},
        };

        for (int[] dir : directions) {
            int ni = i + dir[0];
            int nj = j + dir[1];

            dfs(grid, visited, ni, nj);
        }


    }
    public int numIslands(char[][] grid) {

        int count = 0;
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]){
                    dfs(grid, visited, i, j);
                    count++;
                }
            }
        }
        return count;
    }
}