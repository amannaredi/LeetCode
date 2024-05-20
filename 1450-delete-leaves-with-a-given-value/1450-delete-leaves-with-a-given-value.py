# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rec(root,target):
            if root:
                if root.left:
                    root.left = rec(root.left,target)
                if root.right:
                    root.right = rec(root.right,target)
                if not root.left and not root.right and root.val == target:
                    return None

                return root
                    
            
        return rec(root, target)


        