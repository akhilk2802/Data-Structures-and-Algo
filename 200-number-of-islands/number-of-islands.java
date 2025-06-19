class Solution {

    private void dfs(boolean[][] visited, int i, int j, char[][]grid) {

       if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || visited[i][j] || grid[i][j] != '1'){
        return;
       }
       visited[i][j] = true;

       dfs(visited, i + 1, j, grid);
       dfs(visited, i - 1, j, grid);
       dfs(visited, i, j + 1, grid);
       dfs(visited, i, j - 1, grid);
    }

    public int numIslands(char[][] grid) {

        int m = grid.length;
        int n = grid[0].length;
        int count = 0;

        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j= 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    dfs(visited, i, j, grid);
                    count++;
                }
            }
        }
        return count;
    }
}