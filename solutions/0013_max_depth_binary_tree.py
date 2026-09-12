"""
LeetCode 104: Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Approach: Recursive DFS - depth of tree = 1 + max(depth of left subtree, depth of right subtree)

Time Complexity: O(n) - we visit each node once
Space Complexity: O(h) - where h is height of tree (recursion stack), O(n) worst case for skewed tree
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    """
    Find the maximum depth of a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Maximum depth of the tree (number of nodes on longest path from root to leaf)
    """
    if not root:
        return 0
    
    # Recursively find depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Depth of current node is 1 + max of subtree depths
    return max(left_depth, right_depth) + 1

# Helper function for testing
def build_tree_from_list(values):
    """
    Build a binary tree from a list representation (LeetCode format).
    None represents missing nodes.
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        current = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    
    return root

# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    tree1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    print(f"Tree 1: [3,9,20,null,null,15,7]")
    print(f"Max depth: {max_depth(tree1)}")  # Expected: 3
    print()
    
    # Test case 2: [1,null,2]
    #   1
    #    \
    #     2
    tree2 = build_tree_from_list([1, None, 2])
    print(f"Tree 2: [1,null,2]")
    print(f"Max depth: {max_depth(tree2)}")  # Expected: 2
    print()
    
    # Test case 3: Empty tree
    tree3 = build_tree_from_list([])
    print(f"Tree 3: []")
    print(f"Max depth: {max_depth(tree3)}")  # Expected: 0
    print()
    
    # Test case 4: Single node
    tree4 = build_tree_from_list([1])
    print(f"Tree 4: [1]")
    print(f"Max depth: {max_depth(tree4)}")  # Expected: 1