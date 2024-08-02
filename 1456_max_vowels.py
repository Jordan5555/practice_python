"""

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Link to check: https://www.youtube.com/watch?v=kEfPSzgL-Ss


"""

def maxVowels(s, k):
    
    # Define a set of vowels (both lowercase and uppercase)
    vowels = set('aAeEiIoOuU')

    # Calculate the initial count of vowels in the first 'k' characters of the string 's'
    current_count = sum(char in vowels for char in s[:k])

    # Initialize 'max_count' to the current count of vowels
    max_count = current_count

    # Iterate over the string starting from the 'k-th' character to the end
    for index in range(k, len(s)):
        
        # Add the current character to the current count if it's a vowel
        current_count += s[index] in vowels

        # Subtract the character that's leaving the window from the current count if it's a vowel
        current_count -= s[index - k] in vowels

        # Update the max_count if the current count is greater than the max_count
        max_count = max(current_count, max_count)

    # Return the maximum count of vowels found in any substring of length 'k'
    return max_count


print(maxVowels(s = "abciiidef", k = 3))