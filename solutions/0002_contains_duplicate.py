"""
LeetCode #217: Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def contains_duplicate(nums):
    """
    Determine if array contains duplicates using a set for O(n) lookup.
    
    Approach:
    - Use a set to track seen elements
    - Iterate through array, if element already in set, return True
    - If loop completes without finding duplicates, return False
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(n) - worst case storing all elements in set
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_alternative(nums):
    """
    Alternative approach: compare length of set vs original array.
    
    Time Complexity: O(n) - set creation
    Space Complexity: O(n) - set storage
    """
    return len(nums) != len(set(nums))


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {contains_duplicate(nums1)}")  # Expected: True
    print()
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2}")
    print(f"Output: {contains_duplicate(nums2)}")  # Expected: False
    print()
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3}")
    print(f"Output: {contains_duplicate(nums3)}")  # Expected: True
    print()
    
    # Verify alternative approach gives same results
    print("Verification with alternative approach:")
    print(f"Test 1: {contains_duplicate_alternative(nums1)}")
    print(f"Test 2: {contains_duplicate_alternative(nums2)}")
    print(f"Test 3: {contains_duplicate_alternative(nums3)}")