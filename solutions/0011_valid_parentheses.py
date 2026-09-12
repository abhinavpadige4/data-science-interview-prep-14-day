"""
LeetCode 20: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Approach: Use a stack to track opening brackets. When we see a closing bracket, 
check if it matches the most recent opening bracket.

Time Complexity: O(n) - we traverse the string once
Space Complexity: O(n) - worst case stack size
"""

def is_valid_parentheses(s):
    """
    Determine if a string of parentheses is valid.
    
    Args:
        s: String containing only '(', ')', '{', '}', '[', ']'
        
    Returns:
        True if the string is valid, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            # If it's a closing bracket
            if stack and stack[-1] == bracket_map[char]:
                # Pop the matching opening bracket
                stack.pop()
            else:
                # Either stack is empty or brackets don't match
                return False
        else:
            # If it's an opening bracket, push to stack
            stack.append(char)
    
    # If stack is empty, all brackets were matched properly
    return len(stack) == 0

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {is_valid_parentheses(s1)}")  # Expected: True
    print()
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {is_valid_parentheses(s2)}")  # Expected: True
    print()
    
    # Test case 3
    s3 = "(]"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {is_valid_parentheses(s3)}")  # Expected: False
    print()
    
    # Test case 4
    s4 = "([)]"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {is_valid_parentheses(s4)}")  # Expected: False
    print()
    
    # Test case 5
    s5 = "{[]}"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {is_valid_parentheses(s5)}")  # Expected: True