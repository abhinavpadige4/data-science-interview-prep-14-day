"""
LeetCode 350: Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Approach: Use hash maps to count frequencies, then take minimum counts.

Time Complexity: O(n + m) - where n and m are lengths of the arrays
Space Complexity: O(min(n, m)) - for storing the smaller array's counts
"""

def intersect(nums1, nums2):
    """
    Find intersection of two arrays with proper frequency handling.
    
    Args:
        nums1: First integer array
        nums2: Second integer array
        
    Returns:
        List containing intersection elements with correct frequencies
    """
    # Use the smaller array for the hash map to optimize space
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Count frequencies of elements in nums1
    count_map = {}
    for num in nums1:
        count_map[num] = count_map.get(num, 0) + 1
    
    result = []
    # Check each element in nums2 against the count map
    for num in nums2:
        if num in count_map and count_map[num] > 0:
            result.append(num)
            count_map[num] -= 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Output: {intersect(nums1_1, nums2_1)}")  # Expected: [2, 2]
    print()
    
    # Test case 2
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Output: {intersect(nums1_2, nums2_2)}")  # Expected: [4, 9] or [9, 4]
    print()
    
    # Test case 3
    nums1_3 = [1, 2, 2, 1]
    nums2_3 = [2, 2]
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Output: {intersect(nums1_3, nums2_3)}")  # Expected: [2, 2]