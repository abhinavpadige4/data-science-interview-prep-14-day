"""
LeetCode 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Approach: Use a hash map to store numbers we've seen so far along with their indices.
For each number, check if (target - current_number) exists in the hash map.

Time Complexity: O(n) - we traverse the list once
Space Complexity: O(n) - we store up to n elements in the hash map
"""

def two_sum(nums, target):
    """
    Find two numbers that add up to target and return their indices.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] = target
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")  # Expected: [0, 1]
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")  # Expected: [1, 2]
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")  # Expected: [0, 1]