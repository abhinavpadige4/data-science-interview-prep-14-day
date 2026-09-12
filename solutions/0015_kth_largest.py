"""
LeetCode 215: Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Approach: Use a min-heap of size k to keep track of the k largest elements seen so far.
The root of the heap will be the kth largest element.

Time Complexity: O(n log k) - where n is number of elements, k is the heap size
Space Complexity: O(k) - heap stores at most k elements
"""

import heapq

def find_kth_largest(nums, k):
    """
    Find the kth largest element in an array.
    
    Args:
        nums: List of integers
        k: The kth position to find (1-indexed for largest)
        
    Returns:
        The kth largest element in the array
    """
    # Use a min-heap to store the k largest elements
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        # If heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # The root of the heap is the kth largest element
    return min_heap[0]

# Alternative approach using sorting (less efficient but simpler)
def find_kth_largest_sort(nums, k):
    """
    Find the kth largest element using sorting.
    
    Args:
        nums: List of integers
        k: The kth position to find (1-indexed for largest)
        
    Returns:
        The kth largest element in the array
    """
    nums.sort()
    return nums[-k]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {find_kth_largest(nums1, k1)}")  # Expected: 5
    print()
    
    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {find_kth_largest(nums2, k2)}")  # Expected: 4
    print()
    
    # Test case 3
    nums3 = [1]
    k3 = 1
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {find_kth_largest(nums3, k3)}")  # Expected: 1