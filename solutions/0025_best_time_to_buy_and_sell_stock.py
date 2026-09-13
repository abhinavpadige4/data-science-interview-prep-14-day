"""
LeetCode #121: Best Time to Buy and Sell Stock
Day 14: Light review, behavioral final prep

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

def max_profit(prices: list[int]) -> int:
    """
    Calculate the maximum profit from buying and selling a stock once.
    
    Args:
        prices: List of stock prices where prices[i] is the price on day i
        
    Returns:
        Maximum profit achievable, or 0 if no profit is possible
        
    Time Complexity: O(n) where n is the number of days
    Space Complexity: O(1) - only using two variables
    """
    # Edge case: empty or single element list
    if not prices or len(prices) < 2:
        return 0
    
    # Initialize minimum price to infinity and max profit to 0
    min_price = float('inf')
    max_profit = 0
    
    # Iterate through prices once
    for price in prices:
        # If we find a new minimum price, update it
        if price < min_price:
            min_price = price
        # Otherwise, calculate profit if we sell at current price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    
    return max_profit


def max_profit_brute_force(prices: list[int]) -> int:
    """
    Brute force approach for comparison (O(n^2) time complexity).
    
    Args:
        prices: List of stock prices
        
    Returns:
        Maximum profit achievable
    """
    max_profit = 0
    n = len(prices)
    
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    
    return max_profit


def max_profit_with_days(prices: list[int]) -> tuple[int, int, int]:
    """
    Return maximum profit along with buy and sell days.
    
    Args:
        prices: List of stock prices
        
    Returns:
        Tuple of (max_profit, buy_day, sell_day) where days are 0-indexed
        Returns (0, -1, -1) if no profit is possible
    """
    if not prices or len(prices) < 2:
        return 0, -1, -1
    
    min_price = float('inf')
    max_profit = 0
    buy_day = sell_day = -1
    min_price_day = 0
    
    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            min_price_day = i
        elif price - min_price > max_profit:
            max_profit = price - min_price
            buy_day = min_price_day
            sell_day = i
    
    return max_profit, buy_day, sell_day


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2,3,4,5], 4),
        ([2,4,1], 2),
        ([], 0),
        ([1], 0),
        ([3,3,3,3,3], 0),
        ([1,100], 99),
        ([2,1,2,0,1], 1)
    ]
    
    print("Testing Best Time to Buy and Sell Stock:")
    print("=" * 50)
    
    all_passed = True
    for prices, expected in test_cases:
        result = max_profit(prices)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"prices={prices} -> Output: {result}, Expected: {expected} {status}")
    
    print("=" * 50)
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")
    
    # Demonstrate brute force vs optimized approach
    print("\nPerformance Comparison (on small input):")
    test_prices = [7,1,5,3,6,4]
    brute_result = max_profit_brute_force(test_prices)
    optimized_result = max_profit(test_prices)
    print(f"Brute force result: {brute_result}")
    print(f"Optimized result: {optimized_result}")
    print(f"Results match: {brute_result == optimized_result}")
    
    # Demonstrate the extended function
    print("\nExtended function with buy/sell days:")
    profit, buy_day, sell_day = max_profit_with_days([7,1,5,3,6,4])
    print(f"Max profit: {profit}, Buy on day: {buy_day}, Sell on day: {sell_day}")
    if buy_day != -1 and sell_day != -1:
        print(f"Buy price: {[7,1,5,3,6,4][buy_day]}, Sell price: {[7,1,5,3,6,4][sell_day]}")