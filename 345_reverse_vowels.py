# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


def reverseVowels(s):

    left = 0

    right = len(s)-1

    s = [*s]

    vowels = ['a', 'e', 'i', 'o', 'u']


    while left < right:


        if s[left].lower() not in vowels:
            left += 1

        elif s[right].lower() not in vowels:
            right -= 1
        
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    
    return "".join(s)

print(reverseVowels("leetcode"))