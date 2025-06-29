/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public void dfs(TreeNode root, List<Integer> result) {

        if (root != null) {
            dfs(root.left, result);
            result.add(root.val);
            dfs(root.right, result);
        }

    }

    public TreeNode constructBST(List<Integer> res) {

        if (res.size() == 0 || res == null) {
            return null;
        }

        int mid = res.size() / 2;
        TreeNode root = new TreeNode(res.get(mid));

        root.left = constructBST(res.subList(0, mid));
        root.right = constructBST(res.subList(mid + 1, res.size()));

        return root;

    }
    public TreeNode insertIntoBST(TreeNode root, int val) {

        List<Integer> res = new ArrayList<>();
        dfs(root, res);

        res.add(val);

        Collections.sort(res);
        
        return constructBST(res);        
    }
}