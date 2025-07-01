class Solution {

    public void backtrack(List<Integer> current, int[] candidates, int target, List<List<Integer>> result, int index) {

        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        if (index >= candidates.length || target < 0) {
            return;
        }

        current.add(candidates[index]);
        target -= candidates[index];
        backtrack(current, candidates, target, result, index);
        current.remove(current.size() - 1);
        target += candidates[index];
        backtrack(current, candidates, target, result, index + 1);
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        List<List<Integer>> result = new ArrayList<>();
        backtrack(new ArrayList<>(), candidates, target, result, 0);
        return result;
    }
}