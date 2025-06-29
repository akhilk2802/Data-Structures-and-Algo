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
    public TreeNode bstFromPreorder(int[] preorder) {

        if (preorder.length < 1) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[0]);

        int mid = preorder.length;
        for (int i = 0; i < preorder.length; i++) {
            if (preorder[i] > preorder[0]) {
                mid = i;
                break;
            }
        }

        root.left = bstFromPreorder(Arrays.copyOfRange(preorder, 1, mid));
        root.right = bstFromPreorder(Arrays.copyOfRange(preorder, mid, preorder.length));

        return root;
        
    }
}