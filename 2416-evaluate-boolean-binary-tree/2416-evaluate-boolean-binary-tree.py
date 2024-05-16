# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def inorderTraversal(root):
            if root:
                if root.val == 0:
                    return False
                if root.val == 1:
                    return True
                if root.val == 2:
                    return inorderTraversal(root.left) or inorderTraversal(root.right)
                if root.val == 3:
                    return inorderTraversal(root.left) and inorderTraversal(root.right)
            
        return inorderTraversal(root)
        