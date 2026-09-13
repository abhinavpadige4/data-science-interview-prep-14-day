"""
LeetCode #485: Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""

def find_max_consecutive_ones(nums):
    """
    Find the maximum number of consecutive 1s in a binary array.
    
    Approach:
    - Use a sliding window or two-pointer technique
    - Keep track of current streak of 1s and maximum streak seen
    - Reset current streak when encountering 0
    - Update maximum whenever current streak exceeds it
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using constant extra space
    """
    max_count = 0
    current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0  # Reset streak when encountering 0
    
    return max_count


def find_max_consecutive_ones_alternative(nums):
    """
    Alternative approach: split by zeros and find max length.
    
    Time Complexity: O(n) - split and max operations
    Space Complexity: O(n) - for storing split groups
    """
    # Convert to string, split by '0', find longest segment of '1's
    str_nums = ''.join(map(str, nums))
    groups_of_ones = str_nums.split('0')
    return max(len(group) for group in groups_of_ones) if groups_of_ones else 0


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 0, 1, 1, 1]
    print(f"Input: {nums1}")
    print(f"Output: {find_max_consecutive_ones(nums1)}")  # Expected: 3
    print()
    
    # Test case 2
    nums2 = [1, 0, 1, 1, 0, 1]
    print(f"Input: {nums2}")
    print(f"Output: {find_max_consecutive_ones(nums2)}")  # Expected: 2
    print()
    
    # Additional test cases
    nums3 = [1, 1, 1, 1, 1]
    print(f"Input: {nums3}")
    print(f"Output: {find_max_consecutive_ones(nums3)}")  # Expected: 5
    print()
    
    nums4 = [0, 0, 0, 0]
    print(f"Input: {nums4}")
    print(f"Output: {find_max_consecutive_ones(nums4)}")  # Expected: 0
    print()
    
    nums5 = []
    print(f"Input: {nums5}")
    print(f"Output: {find_max_consecutive_ones(nums5)}")  # Expected: 0
    print()
    
    # Verify alternative approach
    print("Verification with alternative approach:")
    print(f"Test 1: {find_max_consecutive_ones_alternative(nums1)}")
    print(f"Test 2: {find_max_consecutive_ones_alternative(nums2)}")
    print(f"Test 3: {find_max_consecutive_ones_alternative(nums3)}")
    print(f"Test 4: {find_max_consecutive_ones_alternative(nums4)}")
    print(f"Test 5: {find_max_consecutive_ones_alternative(nums5)}")