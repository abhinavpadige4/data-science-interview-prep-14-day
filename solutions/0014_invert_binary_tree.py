"""
LeetCode 226: Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Approach: Recursive approach - swap left and right children of each node.

Time Complexity: O(n) - we visit each node once
Space Complexity: O(h) - where h is height of tree (recursion stack), O(n) worst case for skewed tree
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    """
    Invert a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Root of the inverted binary tree
    """
    if not root:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# Alternative iterative approach using BFS
def invert_tree_iterative(root):
    """
    Invert a binary tree using iterative BFS approach.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Root of the inverted binary tree
    """
    if not root:
        return None
    
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        
        # Swap left and right children
        current.left, current.right = current.right, current.left
        
        # Add children to queue if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return root

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

def tree_to_list(root):
    """
    Convert binary tree to list representation (LeetCode format).
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1: [4,2,7,1,3,6,9]
    #     4
    #    / \
    #   2   7
    #  / \ / \
    # 1  3 6  9
    #
    # After inversion:
    #     4
    #    / \
    #   7   2
    #  / \ / \
    # 9  6 3  1
    tree1 = build_tree_from_list([4, 2, 7, 1, 3, 6, 9])
    inverted1 = invert_tree(tree1)
    print(f"Tree 1: [4,2,7,1,3,6,9]")
    print(f"Inverted: {tree_to_list(inverted1)}")  # Expected: [4,7,2,9,6,3,1]
    print()
    
    # Test case 2: [2,1,3]
    #   2
    #  / \
    # 1   3
    #
    # After inversion:
    #   2
    #  / \
    # 3   1
    tree2 = build_tree_from_list([2, 1, 3])
    inverted2 = invert_tree(tree2)
    print(f"Tree 2: [2,1,3]")
    print(f"Inverted: {tree_to_list(inverted2)}")  # Expected: [2,3,1]
    print()
    
    # Test case 3: Empty tree
    tree3 = build_tree_from_list([])
    inverted3 = invert_tree(tree3)
    print(f"Tree 3: []")
    print(f"Inverted: {tree_to_list(inverted3)}")  # Expected: []
    print()