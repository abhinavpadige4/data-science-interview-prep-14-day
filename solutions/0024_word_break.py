"""
LeetCode #139: Word Break
Day 13: Full-length mock technical interview

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
"""

def word_break(s: str, word_dict: list[str]) -> bool:
    """
    Determine if a string can be segmented into a space-separated sequence of dictionary words.
    
    Args:
        s: Input string to be segmented
        word_dict: List of words available in the dictionary
        
    Returns:
        True if s can be segmented into dictionary words, False otherwise
        
    Time Complexity: O(n^2 * m) where n is length of s and m is average word length
    Space Complexity: O(n) for the DP array
    """
    # Convert word_dict to set for O(1) lookups
    word_set = set(word_dict)
    n = len(s)
    
    # dp[i] will be True if s[0:i] can be segmented into dictionary words
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string can always be segmented
    
    # Build the dp array
    for i in range(1, n + 1):
        # Check all possible splits s[0:j] and s[j:i]
        for j in range(i):
            # If s[0:j] can be segmented AND s[j:i] is in dictionary
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # Found a valid segmentation, no need to check further
    
    return dp[n]


def word_break_with_memoization(s: str, word_dict: list[str]) -> bool:
    """
    Alternative solution using memoization (top-down DP).
    
    Args:
        s: Input string to be segmented
        word_dict: List of words available in the dictionary
        
    Returns:
        True if s can be segmented into dictionary words, False otherwise
    """
    word_set = set(word_dict)
    memo = {}
    
    def can_break(start: int) -> bool:
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and can_break(end):
                memo[start] = True
                return True
        
        memo[start] = False
        return False
    
    return can_break(0)


def word_break_return_sentences(s: str, word_dict: list[str]) -> list[str]:
    """
    Bonus: Return all possible sentences formed by breaking the string using dictionary words.
    
    Args:
        s: Input string to be segmented
        word_dict: List of words available in the dictionary
        
    Returns:
        List of all possible sentences
    """
    word_set = set(word_dict)
    memo = {}
    
    def backtrack(start: int) -> list[str]:
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]
        
        sentences = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                for sentence in backtrack(end):
                    if sentence:
                        sentences.append(word + " " + sentence)
                    else:
                        sentences.append(word)
        
        memo[start] = sentences
        return sentences
    
    return backtrack(0)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("cars", ["car", "ca", "rs"], True),
        ("a", ["b"], False),
        ("aaaaaaa", ["aaaa", "aaa"], True),
        ("leetcodeleet", ["leet", "code"], True)
    ]
    
    print("Testing Word Break:")
    print("=" * 50)
    
    all_passed = True
    for s, word_dict, expected in test_cases:
        result = word_break(s, word_dict)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"s='{s}', dict={word_dict}")
        print(f"  Output: {result}, Expected: {expected} {status}")
        print()
    
    print("=" * 50)
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")
    
    # Demonstrate the bonus function
    print("\nBonus: All possible sentences for 'catsanddog':")
    sentences = word_break_return_sentences("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    for sentence in sentences:
        print(f"  {sentence}")