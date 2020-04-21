from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inOrderTraversal(node): 
    print(f'{node.val}, ', end="")
    if node.left is not None: 
        inOrderTraversal(node.left)
    if node.right is not None: 
        inOrderTraversal(node.right)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) < 1: return None
        return self.BST(preorder, [0], float('inf'))
    
    def BST(self, preorder, cursor, constraint): 
        node = TreeNode(preorder[cursor[0]])
        cursor[0] += 1
        if cursor[0] < len(preorder) and preorder[cursor[0]] < node.val: 
            node.left = self.BST(preorder, cursor, node.val)
        if cursor[0] < len(preorder) and preorder[cursor[0]] < constraint: 
            node.right = self.BST(preorder, cursor, constraint)
        return node 


preorder = [8,5,1,7,10,12]
solution = Solution()
test = solution.bstFromPreorder(preorder)
inOrderTraversal(test)
print()

# tree = TreeNode(8)
# tree.left = TreeNode(5)
# tree.right = TreeNode(10)
# tree.left.left = TreeNode(1)
# tree.left.right = TreeNode(7)
# tree.right.right = TreeNode(12)

# inOrderTraversal(tree)
# print()
