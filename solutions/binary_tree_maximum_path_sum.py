# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root): 
    if root is not None: 
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

class Solution:
    curr_max = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        self.DFS(root)
        return self.curr_max
    
    def DFS(self, root): 
        if root is None: return 0 
        left = max(0, self.DFS(root.left))
        right = max(0, self.DFS(root.right))
        self.curr_max = max(self.curr_max, left + right + root.val)
        return max(left, right) + root.val 
    

tree = TreeNode(-10)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

solution = Solution()
print(solution.maxPathSum(tree))