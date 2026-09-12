"""
LeetCode 5: Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Approach: Expand Around Center - for each character (and between each pair), 
expand outwards as long as we have a palindrome.
We need to check both odd-length and even-length palindromes.

Time Complexity: O(n^2) - we might expand from each center
Space Complexity: O(1) - constant space
"""

def longest_palindrome(s):
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
    
    start = 0
    end = 0
    
    def expand_around_center(left, right):
        """
        Expand outwards from center and return the length of palindrome found.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the actual palindrome boundaries
        return left + 1, right - 1
    
    for i in range(len(s)):
        # Check for odd-length palindromes (center is at i)
        left1, right1 = expand_around_center(i, i)
        # Check for even-length palindromes (center is between i and i+1)
        left2, right2 = expand_around_center(i, i + 1)
        
        # Update if we found a longer palindrome
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    
    return s[start:end+1]

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "babad"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: \"{longest_palindrome(s1)}\"")  # Expected: "bab" or "aba"
    print()
    
    # Test case 2
    s2 = "cbbd"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: \"{longest_palindrome(s2)}\"")  # Expected: "bb"
    print()
    
    # Test case 3
    s3 = "a"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: \"{longest_palindrome(s3)}\"")  # Expected: "a"
    print()
    
    # Test case 4
    s4 = "ac"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: \"{longest_palindrome(s4)}\"")  # Expected: "a" or "c"