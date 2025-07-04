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

    public boolean dfs(TreeNode node, int targetSum, int currSum) {

        if (node == null) {
            return false;
        }

        currSum += node.val;

        if (node.left == null && node.right == null) {
            return currSum == targetSum;
        }

        return (dfs(node.left, targetSum, currSum) || dfs(node.right, targetSum, currSum));
    }

    public boolean hasPathSum(TreeNode root, int targetSum) {

        return dfs(root, targetSum, 0);

    }
}