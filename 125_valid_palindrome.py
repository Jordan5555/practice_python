"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


"""


'Solution 1:' 


import re

def isPalindrome(s: str) -> bool:
    # Convert the string to lowercase to ensure case-insensitive comparison
    clean_s = s.casefold()
    
    # Use regular expression to find all alphanumeric characters in the string
    # re.findall("[a-z0-9]", clean_s) returns a list of matching characters
    clean_lst = re.findall("[a-z0-9]", clean_s)
    
    # Compare the list of alphanumeric characters with its reversed version
    # If they are the same, the string is a palindrome
    return clean_lst == clean_lst[::-1]



'Solution 2:'



def isPalindrome(s):
    # Initialize an empty string to store cleaned characters
    string = ""

    # Iterate over each character in the input string
    for char in s:

        # Check if the character is alphanumeric (a letter or a number)
        if char.isalnum():

            # Convert the character to lowercase and add it to the cleaned string
            string += char.lower()

    # Check if the cleaned string is equal to its reverse
    return string == string[::-1]



'Solution: 3'



def isPalindrome(s):
    
    # Initialize two pointers, left starting at the beginning and right at the end of the string
    left = 0
    right = len(s) - 1

    # Loop until the left pointer is greater than the right pointer
    while left <= right:

        # If the character at the left pointer is not alphanumeric, move the left pointer to the right
        if not s[left].isalnum():
            left += 1

        # If the character at the right pointer is not alphanumeric, move the right pointer to the left
        elif not s[right].isalnum():
            right -= 1

        # If the characters at the left and right pointers are the same (ignoring case), move both pointers inward
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1

        # If the characters at the left and right pointers are different, return False
        else:
            return False

    # If the loop completes without returning False, the string is a palindrome
    return True



print(isPalindrome("race a car"))