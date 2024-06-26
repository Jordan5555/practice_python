# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


def isSubsequence(s, t):

    index1 = 0

    index2 = 0

    while index1 < len(s) and index2 < len(t):
        if s[index1] == t[index2]:
            index1 += 1
        index2 += 1

    return index1 == len(s)

    # return all(ch in t for ch in s) # won't check for order only presence.


print(isSubsequence("abc", "ahgdc"))