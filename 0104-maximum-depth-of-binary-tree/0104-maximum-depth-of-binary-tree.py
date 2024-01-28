# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root)
    
    def dfs(self,root):
        
        if root is None:
            return 0 
        
        else:
            
            return max( 1 + self.dfs(root.left) , 1 + self.dfs(root.right) )
            
    
        