# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            count_1 = 1
            count = 1
            if root.right is not None:
                # 如果右子節點不為空，遞歸計算右子樹的深度
                count += self.maxDepth(root.right)
            if root.left is not None:
                # 如果左子節點不為空，遞歸計算左子樹的深度
                count_1 += self.maxDepth(root.left)

            result = max(count, count_1)
            return result
        
        