"""

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""


'Solution 1:'

def reverseVowels(s):

    # Convert string s into a list of characters
    s = [*s]  

    # Set of vowels (both lowercase and uppercase)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  

    # Pointer for the left end of the string
    left = 0 

    # Pointer for the right end of the string
    right = len(s) - 1

    while left <= right:
        
        if s[left] not in vowels:

            # Move left pointer to the right if the character at left is not a vowel
            left += 1  
            
        elif s[right] not in vowels:

            # Move right pointer to the left if the character at right is not a vowel
            right -= 1  

        else:

            # If both characters at left and right are vowels, swap them
            s[left], s[right] = s[right], s[left]

            # Move left pointer to the right
            left += 1  

            # Move right pointer to the left
            right -= 1 

    # Convert the list back to a string and return
    return "".join(s)


'Solution 2: Time limit exceeded error'

def reverseVowels(s):   

    # Convert string s into a list of characters
    s = [*s]    

    # Set of lowercase vowels
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  
    
    # Iterate through pairs of characters in the string
    for i in range(len(s) - 1):

        for j in range(i + 1, len(s)):

            # Check if both characters at index i and j are vowels (case insensitive)
            if s[i] in vowels and s[j] in vowels:

                # Swap the vowels found at indices i and j
                s[i], s[j] = s[j], s[i]
    
    # Convert the list back to a string and return
    return "".join(s)


print(reverseVowels("leetcode"))