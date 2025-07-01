class Solution {
    public void backtrack(List<List<Integer>> result, int[] candidates, int target, List<Integer> current, int index) {

        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        if (target < 0 || index >= candidates.length) {
            return;
        }

        target -= candidates[index];
        current.add(candidates[index]);
        backtrack(result, candidates, target, current, index + 1);

        current.remove(current.size() - 1);
        target += candidates[index];
        int next = index + 1;
        while (next < candidates.length && candidates[next] == candidates[index]) {
            next += 1;
        }
        backtrack(result, candidates, target, current, next);

    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);

        backtrack(result, candidates, target, new ArrayList<>(), 0);

        return result;
        
    }
}