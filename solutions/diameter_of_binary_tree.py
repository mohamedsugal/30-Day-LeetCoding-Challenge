# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.diameter_helper(root)
    
    def diameter_helper(self, tree: TreeNode) -> int: 
        if tree is None: 
            return 0
        l_height = self.height(tree.left)
        r_height = self.height(tree.right)

        l_diameter = self.diameter_helper(tree.left)
        r_diameter = self.diameter_helper(tree.right)

        return max(l_height + r_height, max(l_diameter, r_diameter))
    
    def height(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

tree = TreeNode(1)
tree.right = TreeNode(3)
tree.left = TreeNode(2)
tree.left.right = TreeNode(5)
tree.left.left = TreeNode(4)

#           1
#         /  \
#        2    3
#      /  \
#     4   5

solution = Solution()
print(solution.diameterOfBinaryTree(tree))