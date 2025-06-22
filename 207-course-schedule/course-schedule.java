class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        

        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adjList.add(new ArrayList<>());
        }

        int[] indegree = new int[numCourses];

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

        int nodes = 0;

        while(!q.isEmpty()) {
            int node = q.poll();
            nodes++;

            for (int n : adjList.get(node)) {
                indegree[n]--;
                if (indegree[n] == 0) {
                    q.offer(n);
                }
            }
        }

        System.out.println("Print, total nodes => " + nodes);
        return nodes == numCourses;
    }
}  