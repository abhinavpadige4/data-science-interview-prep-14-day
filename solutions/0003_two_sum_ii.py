"""
LeetCode 167: Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.

Approach: Use two pointers - one at start, one at end. 
Move pointers based on whether current sum is less than or greater than target.

Time Complexity: O(n) - we traverse the array once with two pointers
Space Complexity: O(1) - constant space
"""

def two_sum_ii(numbers, target):
    """
    Find two numbers in a sorted array that add up to target.
    
    Args:
        numbers: Sorted list of integers (1-indexed for problem)
        target: Target sum
        
    Returns:
        List of two indices [index1, index2] (1-indexed) where numbers[index1] + numbers[index2] = target
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-indexed positions as required by the problem
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # No solution found

# Test cases
if __name__ == "__main__":
    # Test case 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: numbers = {numbers1}, target = {target1}")
    print(f"Output: {two_sum_ii(numbers1, target1)}")  # Expected: [1, 2]
    print()
    
    # Test case 2
    numbers2 = [2, 3, 4]
    target2 = 6
    print(f"Input: numbers = {numbers2}, target = {target2}")
    print(f"Output: {two_sum_ii(numbers2, target2)}")  # Expected: [1, 3]
    print()
    
    # Test case 3
    numbers3 = [-1, 0]
    target3 = -1
    print(f"Input: numbers = {numbers3}, target = {target3}")
    print(f"Output: {two_sum_ii(numbers3, target3)}")  # Expected: [1, 2]