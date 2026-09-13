"""
LeetCode #66: Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

def plus_one(digits):
    """
    Increment a large integer represented as an array by one.
    
    Approach:
    - Start from the least significant digit (end of array)
    - Add one and handle carry propagation
    - If we reach the most significant digit and still have carry, prepend 1
    
    Time Complexity: O(n) - worst case we traverse all digits
    Space Complexity: O(1) - modify in place, or O(n) if we need new array for all 9s case
    """
    n = len(digits)
    
    # Start from the end and move backwards
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # Set to 0 and carry over to next digit
    
    # If we get here, all digits were 9, so we need an extra digit at the front
    return [1] + digits


def plus_one_alternative(digits):
    """
    Alternative approach: convert to string, increment, convert back.
    Less efficient but more readable.
    
    Time Complexity: O(n) - string conversion and manipulation
    Space Complexity: O(n) - for string and result array
    """
    num_str = ''.join(map(str, digits))
    incremented = str(int(num_str) + 1)
    return [int(digit) for digit in incremented]


# Test cases
if __name__ == "__main__":
    # Test case 1
    digits1 = [1, 2, 3]
    print(f"Input: {digits1}")
    print(f"Output: {plus_one(digits1.copy())}")  # Expected: [1,2,4]
    print()
    
    # Test case 2
    digits2 = [4, 3, 2, 1]
    print(f"Input: {digits2}")
    print(f"Output: {plus_one(digits2.copy())}")  # Expected: [4,3,2,2]
    print()
    
    # Test case 3
    digits3 = [9]
    print(f"Input: {digits3}")
    print(f"Output: {plus_one(digits3.copy())}")  # Expected: [1,0]
    print()
    
    # Additional test case: all 9s
    digits4 = [9, 9, 9]
    print(f"Input: {digits4}")
    print(f"Output: {plus_one(digits4.copy())}")  # Expected: [1,0,0,0]
    print()
    
    # Verify alternative approach
    print("Verification with alternative approach:")
    print(f"Test 1: {plus_one_alternative(digits1)}")
    print(f"Test 2: {plus_one_alternative(digits2)}")
    print(f"Test 3: {plus_one_alternative(digits3)}")
    print(f"Test 4: {plus_one_alternative(digits4)}")