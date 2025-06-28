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

    public void dfs(TreeNode node, List<Integer> result, int height) {

        if (node == null){
            return;
        }

        if (result.size() == height) {
            result.add(node.val);
        }

        dfs(node.right, result, height + 1);
        dfs(node.left, result, height + 1);
    }

    public List<Integer> rightSideView(TreeNode root) {
        
        List<Integer> result = new ArrayList<>();
        dfs(root, result, 0);

        return result;
    }
}