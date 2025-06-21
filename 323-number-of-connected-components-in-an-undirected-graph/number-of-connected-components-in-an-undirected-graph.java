
import java.awt.Component;class Solution {
    public int countComponents(int n, int[][] edges) {

        List<List<Integer>> adjList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }
        
        boolean[] visited = new boolean[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, visited, adjList);
                count++;
            }
        }
        return count;
    }

    public void bfs(int node, boolean[] visited, List<List<Integer>> adjList) {

        Queue<Integer> q = new LinkedList<>();
        q.offer(node);
        visited[node] = true;

        while (!q.isEmpty()) {
            int loc = q.poll();

            for (int n : adjList.get(loc)){
                if (!visited[n]) {
                    q.offer(n);
                    visited[n] = true;
                }
            }
        }
    }

    // public void dfs(int node, boolean[] visited, List<List<Integer>> adjList) {

    //     visited[node] = true;

    //     for (int n : adjList.get(node)) {
    //         if (!visited[n]) {
    //             dfs(n, visited, adjList);
    //         }
    //     }
    // }
}