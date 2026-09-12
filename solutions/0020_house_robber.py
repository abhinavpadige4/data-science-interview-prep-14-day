"""
LeetCode 198: House Robber
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses 
have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Approach: Dynamic Programming - at each house, we have two choices:
1. Rob this house + money from houses up to i-2
2. Skip this house + money from houses up to i-1
dp[i] = max(dp[i-1], dp[i-2] + nums[i])

Time Complexity: O(n) - we compute each value once
Space Complexity: O(1) - we only need to store the last two values
"""

def rob(nums):
    """
    Calculate the maximum amount of money that can be robbed without alerting police.
    
    Args:
        nums: List of integers representing money in each house
        
    Returns:
        Maximum amount of money that can be robbed
    """
    if not nums:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    # Use two variables to store the last two results (space optimization)
    prev2 = nums[0]                           # max money up to house i-2
    prev1 = max(nums[0], nums[1])             # max money up to house i-1
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1

# Alternative DP approach with array (less space efficient but clearer)
def rob_dp(nums):
    """
    Calculate the maximum amount of money that can be robbed using DP array.
    
    Args:
        nums: List of integers representing money in each house
        
    Returns:
        Maximum amount of money that can be robbed
    """
    if not nums:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    # dp[i] = max money that can be robbed from houses[0:i+1]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {rob(nums1)}")  # Expected: 4
    print()
    
    # Test case 2
    nums2 = [2, 7, 9, 3, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {rob(nums2)}")  # Expected: 12
    print()
    
    # Test case 3
    nums3 = [2, 1, 1, 2]
    print(f"Input: nums = {nums3}")
    print(f"Output: {rob(nums3)}")  # Expected: 4
    print()
    
    # Test case 4
    nums4 = [2]
    print(f"Input: nums = {nums4}")
    print(f"Output: {rob(nums4)}")  # Expected: 2
    print()
    
    # Test case 5
    nums5 = []
    print(f"Input: nums = {nums5}")
    print(f"Output: {rob(nums5)}")  # Expected: 0