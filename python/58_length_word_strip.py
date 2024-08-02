"""

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.


"""


'Solution 1:'

def lengthOfLastWor(s):
  
  # Split the string and return length of last word. Splitting takes care of stripping
  return len(s.split()[-1])



'Solution 2:'


def lengthOfLastWord(s):
    
    # Initialize end_index to the last character's index of the string
    end_index = len(s) - 1

    # Skip trailing spaces by moving end_index to the left
    while end_index >= 0 and s[end_index] == " ":
        end_index -= 1

    # Initialize start_index to the current position of end_index
    start_index = end_index

    # Move start_index to the left until a space is encountered or the beginning of the string is reached
    while start_index >= 0 and s[start_index] != " ":
        start_index -= 1

    # The length of the last word is the difference between end_index and start_index
    return end_index - start_index


print(lengthOfLastWor("   fly me   to   the moon  "))