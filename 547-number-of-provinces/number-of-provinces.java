class Solution {
    public void dfs(int i, boolean[] visited, List<List<Integer>> adjList) {
        visited[i] = true;
        for (int n : adjList.get(i)){
            if (!visited[n]) {
                dfs(n, visited, adjList);
            }
        }
    };

    public void bfs(int i, boolean[] visited, List<List<Integer>> adjList) {

        Queue<Integer> q = new LinkedList<>();
        q.offer(i);
        visited[i] = true;

        while (!q.isEmpty()) {
            int node = q.poll();

            for (int n : adjList.get(node)){
                if (!visited[n]){
                    q.offer(n);
                    visited[n] = true;

                }
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        List<List<Integer>> adjList = new ArrayList<>();
        int n = isConnected.length;

        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
            for (int j = 0; j < n; j++){
                if (i != j && isConnected[i][j] == 1){
                    adjList.get(i).add(j);
                }
            }
        }
        int count = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, visited, adjList);
                count++;
            }
        }
        return count;
    }
}