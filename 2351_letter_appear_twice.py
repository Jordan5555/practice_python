"""

Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
 

Example 1:

Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
Example 2:

Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.


"""


'Solution 1: wont work, against requirements'

def repeatedCharacter(s):

    # Initialize index to traverse through the string
    i = 0  
    
    # Loop through the string up to the second last character
    while i < len(s) - 1:

        # Check if current character is equal to the next character
        if s[i] == s[i + 1]:  

            # Return the repeated character if found
            return s[i]  
        
        # Move to the next character if no repetition is found
        else:
            i += 1  
    
    # Return False if no repeated character is found in the string
    return False  



'Solution 2:'



def repeatedCharacter(s):

    # Initialize an empty set to store unique characters encountered
    unique = set()  
    
    # Iterate through each character in the string s
    for char in s:  

        # Check if the character is already in the set
        if char in unique:

            # Return the character if it is repeated
            return char  

        # Add the character to the set if it is not repeated
        unique.add(char)  
    
    # Return None if no character is repeated in the string
    return None


'Solution 3:'

def repeatedCharacter(s):

    # Initialize an empty dictionary to store character frequencies
    d = {}  
    
    # Iterate through each character in the string s
    for char in s:

        # Check if the character is already in the dictionary
        if char in d:  

            # Return the character if it is repeated
            return char  
        
        # Add the character to the dictionary with frequency 1
        d[char] = 1  
    
    # Return None if no character is repeated in the string
    return None  
