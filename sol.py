# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tree_level(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        else:
            return 1 + self.tree_level(root.left)

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        left_tree_level = self.tree_level(root.left)
        right_tree_level = self.tree_level(root.right)

        if left_tree_level == right_tree_level:
            return pow(2, left_tree_level) + self.countNodes(root.right)
        else:
            return pow(2, right_tree_level) + self.countNodes(root.left)