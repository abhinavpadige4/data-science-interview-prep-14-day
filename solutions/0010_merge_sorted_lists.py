"""
LeetCode 21: Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Approach: Use a dummy head and compare nodes from both lists, appending the smaller one.

Time Complexity: O(n + m) - where n and m are lengths of the two lists
Space Complexity: O(1) - constant space (excluding output)
"""

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    """
    Merge two sorted linked lists.
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Create a dummy node to serve as the start of the result list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining part of either list
    current.next = list1 if list1 else list2
    
    return dummy.next

# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [1,2,4], list2 = [1,3,4]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [1,1,2,3,4,4]
    print()
    
    # Test case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [], list2 = []")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: []
    print()
    
    # Test case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [], list2 = [0]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [0]