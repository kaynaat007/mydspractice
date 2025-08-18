class TreeNode(var `val`: Int)
{
    var left: TreeNode? = null
    var right: TreeNode? = null
}




/**
 *  if targetSum is present from root to leaf
 *   5
 *  / \
 *  3  8
 *
 *  target = 13
 */
fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {

     if (root == null) {
         return false
     }

     if (root.left == null  && root.right == null && targetSum - root.`val` == 0) {
         return true
     }

    return hasPathSum(root.left, targetSum - root.`val`) || hasPathSum(root.right, targetSum - root.`val`)


}

val root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)



print(hasPathSum(root, 3))