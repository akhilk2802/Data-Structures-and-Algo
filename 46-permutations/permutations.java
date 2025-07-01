class Solution {
    public List<List<Integer>> permute(int[] nums) {

        if (nums.length == 0) {
            List<List<Integer>> base = new ArrayList<>();
            base.add(new ArrayList<>());
            return base;
        }

        int first = nums[0];
        int[] rest = Arrays.copyOfRange(nums, 1, nums.length);
        List<List<Integer>> perms = permute(rest);

        List<List<Integer>> result = new ArrayList<>();

        for (List<Integer> perm : perms) {
            for (int i = 0; i <= perm.size(); i++) {
                List<Integer> temp = new ArrayList<>(perm);
                temp.add(i, first);
                result.add(temp);
            }
        }

        return result;

    }
}