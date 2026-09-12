"""
LeetCode 209: Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Approach: Sliding window technique - expand window until sum >= target, then contract from left.

Time Complexity: O(n) - each element visited at most twice
Space Complexity: O(1) - constant space
"""

def min_sub_array_len(target, nums):
    """
    Find the minimal length of a contiguous subarray of which the sum >= target.
    
    Args:
        target: Target sum
        nums: List of positive integers
        
    Returns:
        Minimal length of subarray with sum >= target, or 0 if no such subarray exists
    """
    if not nums:
        return 0
    
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Shrink window from left as much as possible while sum >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return 0 if min_length == float('inf') else min_length

# Test cases
if __name__ == "__main__":
    # Test case 1
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    print(f"Input: target = {target1}, nums = {nums1}")
    print(f"Output: {min_sub_array_len(target1, nums1)}")  # Expected: 2
    print()
    
    # Test case 2
    target2 = 4
    nums2 = [1, 4, 4]
    print(f"Input: target = {target2}, nums = {nums2}")
    print(f"Output: {min_sub_array_len(target2, nums2)}")  # Expected: 1
    print()
    
    # Test case 3
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
    print(f"Input: target = {target3}, nums = {nums3}")
    print(f"Output: {min_sub_array_len(target3, nums3)}")  # Expected: 0