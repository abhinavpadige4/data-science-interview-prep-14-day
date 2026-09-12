"""
LeetCode 322: Coin Change
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Approach: Dynamic Programming - bottom-up approach.
dp[i] = minimum number of coins to make amount i
dp[i] = min(dp[i], dp[i - coin] + 1) for each coin in coins

Time Complexity: O(amount * len(coins)) - we compute each amount for each coin
Space Complexity: O(amount) - dp array of size amount+1
"""

def coin_change(coins, amount):
    """
    Find the fewest number of coins needed to make up the given amount.
    
    Args:
        coins: List of coin denominations
        amount: Target amount of money
        
    Returns:
        Fewest number of coins needed, or -1 if not possible
    """
    # Edge case: amount is 0
    if amount == 0:
        return 0
    
    # Initialize dp array with infinity (unreachable)
    # dp[i] = minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
    # Build up the solution from 1 to amount
    for i in range(1, amount + 1):
        # Try each coin
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result if reachable, otherwise -1
    return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
if __name__ == "__main__":
    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Output: {coin_change(coins1, amount1)}")  # Expected: 3 (5+5+1 or 5+2+2+2)
    print()
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"Input: coins = {coins2}, amount = {amount2}")
    print(f"Output: {coin_change(coins2, amount2)}")  # Expected: -1
    print()
    
    # Test case 3
    coins3 = [1]
    amount3 = 0
    print(f"Input: coins = {coins3}, amount = {amount3}")
    print(f"Output: {coin_change(coins3, amount3)}")  # Expected: 0
    print()
    
    # Test case 4
    coins4 = [1, 2, 5]
    amount4 = 100
    print(f"Input: coins = {coins4}, amount = {amount4}")
    print(f"Output: {coin_change(coins4, amount4)}")  # Expected: 20 (20*5)