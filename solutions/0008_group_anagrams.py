"""
LeetCode 49: Group Anagrams
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Approach: Sort each string to create a canonical form, then group by sorted version.

Time Complexity: O(n * k log k) - where n is number of strings, k is max length of string
Space Complexity: O(n * k) - storing all strings in groups
"""

from collections import defaultdict

def group_anagrams(strs):
    """
    Group anagrams together from a list of strings.
    
    Args:
        strs: List of strings
        
    Returns:
        List of lists, where each inner list contains anagrams grouped together
    """
    # Map sorted string -> list of original strings that are anagrams
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort the string to create canonical form
        sorted_s = ''.join(sorted(s))
        anagram_map[sorted_s].append(s)
    
    # Return all groups
    return list(anagram_map.values())

# Test cases
if __name__ == "__main__":
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: strs = {strs1}")
    print(f"Output: {group_anagrams(strs1)}")
    # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]] (order may vary)
    print()
    
    # Test case 2
    strs2 = [""]
    print(f"Input: strs = {strs2}")
    print(f"Output: {group_anagrams(strs2)}")  # Expected: [[""]]
    print()
    
    # Test case 3
    strs3 = ["a"]
    print(f"Input: strs = {strs3}")
    print(f"Output: {group_anagrams(strs3)}")  # Expected: [["a"]]