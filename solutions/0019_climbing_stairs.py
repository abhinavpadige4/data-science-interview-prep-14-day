"""
LeetCode 70: Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Approach: Dynamic Programming - this is essentially the Fibonacci sequence.
ways[n] = ways[n-1] + ways[n-2]

Time Complexity: O(n) - we compute each value once
Space Complexity: O(1) - we only need to store the last two values
"""

def climb_stairs(n):
    """
    Calculate the number of distinct ways to climb to the top of a staircase.
    
    Args:
        n: Number of steps to reach the top
        
    Returns:
        Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
    
    # Use two variables to store the last two results (space optimization)
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Alternative DP approach with array (less space efficient but clearer)
def climb_stairs_dp(n):
    """
    Calculate the number of distinct ways to climb to the top using DP array.
    
    Args:
        n: Number of steps to reach the top
        
    Returns:
        Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
    
    # dp[i] = number of ways to reach step i
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way to reach step 1
    dp[2] = 2  # 2 ways to reach step 2 (1+1 or 2)
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Test cases
if __name__ == "__main__":
    # Test case 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Output: {climb_stairs(n1)}")  # Expected: 2
    print()
    
    # Test case 2
    n2 = 3
    print(f"Input: n = {n2}")
    print(f"Output: {climb_stairs(n2)}")  # Expected: 3
    print()
    
    # Test case 3
    n3 = 4
    print(f"Input: n = {n3}")
    print(f"Output: {climb_stairs(n3)}")  # Expected: 5
    print()
    
    # Test case 4
    n4 = 1
    print(f"Input: n = {n4}")
    print(f"Output: {climb_stairs(n4)}")  # Expected: 1