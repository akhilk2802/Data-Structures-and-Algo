class Solution {

    public void backtrack(List<Integer> current, int[] nums, int index, List<List<Integer>> result){

        int n = nums.length;
        if (index == n) {
            result.add(new ArrayList<>(current));
            return;
        }

        current.add(nums[index]);
        backtrack(current, nums, index + 1, result);
        current.remove(current.size() - 1);
        backtrack(current, nums, index + 1, result);
    }

    public List<List<Integer>> subsets(int[] nums) {

        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();

        backtrack(new ArrayList<>(), nums, 0, result);

        return result;
    }
}