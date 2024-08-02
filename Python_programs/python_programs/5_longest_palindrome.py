"""

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

Link to check: https://www.youtube.com/watch?v=0CKUjDcUYYA


"""


def longestPalindrome(s):

    # Helper function to expand around the center and return the longest palindromic substring
    def expand(left, right):

        # Expand as long as the characters on the left and right are equal and within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # Return the palindromic substring found
        return s[left+1:right]
    
    # Initialize the result to store the longest palindromic substring found
    result = ""  

    # Iterate through each character in the string
    for i in range(len(s)):

        # Check for the longest odd-length palindrome centered at i
        sub1 = expand(i, i)

        # Update the result if the found palindrome is longer than the current result
        if len(sub1) > len(result):
            result = sub1

        # Check for the longest even-length palindrome centered between i and i+1
        sub2 = expand(i, i + 1)
        
        # Update the result if the found palindrome is longer than the current result
        if len(sub2) > len(result):
            result = sub2

    # Return the longest palindromic substring found
    return result
