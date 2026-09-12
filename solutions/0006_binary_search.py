"""
LeetCode 704: Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

Approach: Classic binary search algorithm - divide and conquer.

Time Complexity: O(log n) - we halve the search space each iteration
Space Complexity: O(1) - constant space
"""

def search(nums, target):
    """
    Search for target in sorted array using binary search.
    
    Args:
        nums: Sorted list of integers in ascending order
        target: Integer to search for
        
    Returns:
        Index of target if found, otherwise -1
    """
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents potential overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {search(nums1, target1)}")  # Expected: 4
    print()
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {search(nums2, target2)}")  # Expected: -1
    print()
    
    # Test case 3
    nums3 = [5]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {search(nums3, target3)}")  # Expected: 0
    print()
    
    # Test case 4
    nums4 = []
    target4 = 5
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {search(nums4, target4)}")  # Expected: -1