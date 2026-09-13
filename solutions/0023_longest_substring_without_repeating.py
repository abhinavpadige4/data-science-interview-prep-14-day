"""
LeetCode #3: Longest Substring Without Repeating Characters
Day 12: Review weak areas, mixed practice

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
        
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(min(m, n)) where m is the size of the charset
    """
    # Sliding window approach with hash map to track character indices
    char_index_map = {}
    max_length = 0
    start = 0  # Start of the current window
    
    for end in range(len(s)):
        # If character is already in the current window, move start pointer
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        
        # Update the character's latest index
        char_index_map[s[end]] = end
        
        # Update max length if current window is larger
        max_length = max(max_length, end - start + 1)
    
    return max_length


def length_of_longest_substring_brute_force(s: str) -> int:
    """
    Brute force approach for comparison (O(n^3) time complexity).
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    max_length = 0
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if len(set(substring)) == len(substring):  # All characters are unique
                max_length = max(max_length, len(substring))
    
    return max_length


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("dvdf", 3),
        ("anviaj", 5),
        ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 62)
    ]
    
    print("Testing Longest Substring Without Repeating Characters:")
    print("=" * 60)
    
    all_passed = True
    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"Input: '{s}' -> Output: {result}, Expected: {expected} {status}")
    
    print("=" * 60)
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")
    
    # Demonstrate brute force vs optimized approach
    print("\nPerformance Comparison (on small input):")
    test_str = "abcabcbb"
    brute_result = length_of_longest_substring_brute_force(test_str)
    optimized_result = length_of_longest_substring(test_str)
    print(f"Brute force result: {brute_result}")
    print(f"Optimized result: {optimized_result}")
    print(f"Results match: {brute_result == optimized_result}")