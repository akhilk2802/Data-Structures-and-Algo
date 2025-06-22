class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {

        List<List<Integer>> adjList = new ArrayList<>();
        int[] indegree = new int[numCourses];

        for (int i = 0 ; i < numCourses; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int[] prereq : prerequisites) {
            int course = prereq[0];
            int prerequisite = prereq[1];

            adjList.get(prerequisite).add(course);
            indegree[course]++;
        }
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0) {
                q.offer(i);
            }
        }

        int[] topoOrder = new int[numCourses];
        int index = 0;

        while (!q.isEmpty()) {
            int node = q.poll();
            topoOrder[index] = node;
            index++;

            for (int neighbor : adjList.get(node)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.offer(neighbor);
                }
            }
        }

        return index == numCourses ? topoOrder : new int[0];
    }
}