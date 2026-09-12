"""
LeetCode 7: Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Approach: Extract digits from the end and build the reversed number.
Handle overflow by checking against 32-bit integer limits.

Time Complexity: O(log(x)) - number of digits in x
Space Complexity: O(1) - constant space
"""

def reverse_integer(x):
    """
    Reverse the digits of a 32-bit signed integer.
    
    Args:
        x: Integer to reverse
        
    Returns:
        Reversed integer or 0 if overflow occurs
    """
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    
    reversed_num = 0
    while x_abs > 0:
        digit = x_abs % 10
        # Check for overflow before actually adding the digit
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        reversed_num = reversed_num * 10 + digit
        x_abs //= 10
    
    return sign * reversed_num

# Test cases
if __name__ == "__main__":
    # Test case 1
    x1 = 123
    print(f"Input: x = {x1}")
    print(f"Output: {reverse_integer(x1)}")  # Expected: 321
    print()
    
    # Test case 2
    x2 = -123
    print(f"Input: x = {x2}")
    print(f"Output: {reverse_integer(x2)}")  # Expected: -321
    print()
    
    # Test case 3
    x3 = 120
    print(f"Input: x = {x3}")
    print(f"Output: {reverse_integer(x3)}")  # Expected: 21
    print()
    
    # Test case 4 - Overflow case
    x4 = 1534236469
    print(f"Input: x = {x4}")
    print(f"Output: {reverse_integer(x4)}")  # Expected: 0 (overflow)