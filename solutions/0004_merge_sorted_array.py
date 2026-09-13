"""
LeetCode #88: Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note: Because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays into nums1 in-place.
    
    Approach:
    - Use three pointers starting from the end
    - p1 points to last valid element in nums1
    - p2 points to last element in nums2
    - p points to last position in nums1 (m+n-1)
    - Compare elements and place larger one at position p
    - Decrement appropriate pointers
    
    Time Complexity: O(m+n) - single pass through both arrays
    Space Complexity: O(1) - in-place modification
    """
    # Pointers for nums1 (valid elements), nums2, and merge position
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    # Merge from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2, copy them
    # (No need to copy from nums1 as they're already in place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


def merge_alternative(nums1, m, nums2, n):
    """
    Alternative approach: copy nums2 to nums1 then sort.
    Less efficient but simpler.
    
    Time Complexity: O((m+n) log(m+n)) - due to sorting
    Space Complexity: O(1) - in-place
    """
    # Copy elements from nums2 to nums1
    for i in range(n):
        nums1[m + i] = nums2[i]
    
    # Sort the entire nums1 array
    nums1[:m+n] = sorted(nums1[:m+n])


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    nums2_1 = [2, 5, 6]
    n1 = 3
    merge(nums1_1, m1, nums2_1, n1)
    print(f"Test 1:")
    print(f"nums1 after merge: {nums1_1}")  # Expected: [1,2,2,3,5,6]
    print()
    
    # Test case 2
    nums1_2 = [1]
    m2 = 1
    nums2_2 = []
    n2 = 0
    merge(nums1_2, m2, nums2_2, n2)
    print(f"Test 2:")
    print(f"nums1 after merge: {nums1_2}")  # Expected: [1]
    print()
    
    # Test case 3
    nums1_3 = [0]
    m3 = 0
    nums2_3 = [1]
    n3 = 1
    merge(nums1_3, m3, nums2_3, n3)
    print(f"Test 3:")
    print(f"nums1 after merge: {nums1_3}")  # Expected: [1]
    print()
    
    # Additional test case
    nums1_4 = [4, 5, 6, 0, 0, 0]
    m4 = 3
    nums2_4 = [1, 2, 3]
    n4 = 3
    merge(nums1_4, m4, nums2_4, n4)
    print(f"Test 4:")
    print(f"nums1 after merge: {nums1_4}")  # Expected: [1,2,3,4,5,6]
    print()
    
    # Verify alternative approach
    print("Verification with alternative approach:")
    nums1_alt = [1, 2, 3, 0, 0, 0]
    merge_alternative(nums1_alt, 3, [2, 5, 6], 3)
    print(f"Alternative result: {nums1_alt}")