class Solution {
    public int dfs(int i, int j, int[][] grid, boolean[][] visited) {
        
        int m = grid.length;
        int n = grid[0].length;

        if(i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != 1 || visited[i][j]){
            return 0;
        }

        visited[i][j] = true;
        int area = 1;

        area += dfs(i + 1, j, grid, visited);
        area += dfs(i - 1, j, grid, visited);
        area += dfs(i, j + 1, grid, visited);
        area += dfs(i, j - 1, grid, visited);

        return area;
    }

    public int maxAreaOfIsland(int[][] grid) {

        int area = 0;

        int m = grid.length;
        int n = grid[0].length;

        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && grid[i][j] == 1){
                    int currentArea = 0;
                    currentArea = dfs(i, j, grid, visited);
                    area = Math.max(area, currentArea);
                }
            }
        }
        return area;
    }
}