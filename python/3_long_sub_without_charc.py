"""

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


"""

def lengthOfLongestSubstring(s):

    # Initialize the left pointer of the sliding window
    left = 0      
    
    # Initialize the right pointer of the sliding window        
    right = 0             

    # Initialize a set to keep track of unique characters in the current window
    unique_char = set() 

    # Variable to keep track of the maximum length of substring without repeating characters
    max_len = 0           

    # Loop until the right pointer reaches the end of the string
    while right < len(s):  

        # If the character at the right pointer is not in the set
        if s[right] not in unique_char:  

            # Add it to the set
            unique_char.add(s[right])    

            # Update max_len if the current window is larger
            max_len = max(max_len, right - left + 1)  
            
            # Move the right pointer to the right to expand the window
            right += 1  

        # If the character at the right pointer is already in the set
        else:  

            # Remove the character at the left pointer from the set
            unique_char.remove(s[left])  

            # Move the left pointer to the right to shrink the window and remove duplicates
            left += 1  

    # Return the maximum length of substring without repeating characters found
    return max_len  
