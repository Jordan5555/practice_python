"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""


import re
def isPalindrome(s: str) -> bool:
  clean_lst = re.findall("[a-z0-9]", s.casefold())
  return clean_lst == clean_lst[::-1]


def isPalindrome(self, s: str) -> bool:
    sen = ""
    for c in s:
        if c.isalnum():
            sen += c
    sen = sen.lower()
    return sen == sen[::-1]


def isPalindrome(s: str):
    
    left = 0
    right = len(s) - 1

    while left < right:
        
        if not s[left].isalnum():
            left += 1

        elif not s[right].isalnum():
            right -= 1

        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1

        else:                        
            return False
        
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))