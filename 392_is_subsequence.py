"""

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

"""



'Solution 1:'

def isSubsequence(s, t):

    # Initialize pointers for both strings
    index1 = 0
    index2 = 0

    # Loop through both strings until we reach the end of one of them
    while index1 < len(s) and index2 < len(t):

        # If characters match, move the pointer of s to the next character
        if s[index1] == t[index2]:
            index1 += 1

        # Always move the pointer of t to the next character
        index2 += 1

    # If we have traversed the entire s, it means s is a subsequence of t
    return index1 == len(s)


'Solution 2: '


def isSubsequence(s, t):
  
    # Create an iterator for the string t
    t_iter = iter(t)

    # Check if all characters of s can be found in t_iter
    return all(char in t_iter for char in s)


print(isSubsequence("abc", "ahgdc"))