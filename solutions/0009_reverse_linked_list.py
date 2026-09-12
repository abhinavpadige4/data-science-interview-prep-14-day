"""
LeetCode 206: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach: Iterative approach using three pointers - prev, current, next.

Time Complexity: O(n) - we traverse the list once
Space Complexity: O(1) - constant space
"""

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        New head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_node = current.next
        # Reverse current node's pointer
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_node
    
    # Prev will be the new head
    return prev

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
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed_head1 = reverse_linked_list(head1)
    print(f"Input: [1,2,3,4,5]")
    print(f"Output: {linked_list_to_list(reversed_head1)}")  # Expected: [5,4,3,2,1]
    print()
    
    # Test case 2
    head2 = create_linked_list([1, 2])
    reversed_head2 = reverse_linked_list(head2)
    print(f"Input: [1,2]")
    print(f"Output: {linked_list_to_list(reversed_head2)}")  # Expected: [2,1]
    print()
    
    # Test case 3
    head3 = create_linked_list([])
    reversed_head3 = reverse_linked_list(head3)
    print(f"Input: []")
    print(f"Output: {linked_list_to_list(reversed_head3)}")  # Expected: []