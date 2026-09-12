"""
LeetCode 347: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Approach: Use hash map to count frequencies, then use min-heap of size k to get top k frequent elements.

Time Complexity: O(n + m log k) - where n is number of elements, m is number of unique elements
Space Complexity: O(n) - for storing frequency map and heap
"""

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """
    Find the k most frequent elements in an array.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Use a min-heap to keep track of top k frequent elements
    # We store (-frequency, element) to simulate max-heap behavior with min-heap
    min_heap = []
    
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        # If heap size exceeds k, remove the least frequent element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract elements from heap (ignore frequencies)
    return [num for freq, num in min_heap]

# Alternative approach using bucket sort (O(n) time)
def top_k_frequent_bucket_sort(nums, k):
    """
    Find the k most frequent elements using bucket sort.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Create buckets where index = frequency
    max_freq = len(nums)
    buckets = [[] for _ in range(max_freq + 1)]
    
    # Place elements in buckets based on their frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect top k frequent elements from buckets (highest frequency first)
    result = []
    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {top_k_frequent(nums1, k1)}")  # Expected: [1, 2] (order may vary)
    print()
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {top_k_frequent(nums2, k2)}")  # Expected: [1]
    print()
    
    # Test case 3
    nums3 = [1, 2]
    k3 = 2
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {top_k_frequent(nums3, k3)}")  # Expected: [1, 2] (order may vary)