# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.



words = ["Flower", "Flow", "Flight"]


'Solution 1:'

def longestCommonPrefix(words):
    
    # Find the shortest word in the list 'words' to use as an initial prefix
    prefix = min(words, key=len)

    # Iterate over each word in the list
    for word in words:
        
        # While the current word does not start with the prefix
        while not word.startswith(prefix):
            
            # Remove the last character from the prefix
            prefix = prefix[:-1]

            # If the prefix becomes an empty string, return it immediately
            if not prefix:
                return ""

    # Return the longest common prefix found
    return prefix

# Example usage:
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"



'Solution 2:'


def longestCommonPrefix(strs):
    
    # Find the shortest word in the list 'strs' to use as an initial prefix
    prefix = min(strs, key=len)

    # Iterate over each character index in the prefix
    for index in range(len(prefix)):
        
        # Iterate over each word in the list 'strs'
        for char in strs:
            
            # If the current index is out of bounds for the current word
            # or the character at the current index in the word does not match the prefix
            if index >= len(char) or char[index] != prefix[index]:
                
                # Return the substring of the prefix up to but not including the current index
                return prefix[:index]

    # If the loop completes, the entire prefix is common to all words, return the prefix
    return prefix

# Example usage:
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"

                

'Solution 3:'


def longestCommonPrefix(strs):

    # Edge case: If the list is empty, return an empty string
    if not strs:
        return ""
    
    # Find the lexicographically smallest and largest strings in the list
    a = min(strs)
    b = max(strs)

    # Initialize a pointer j to iterate over the characters
    j = 0

    # Iterate while j is within the bounds of both strings and the characters match
    while j < len(a) and j < len(b) and a[j] == b[j]:
        j += 1

    # The longest common prefix is the substring of 'a' up to the index j
    return a[:j]

# Example usage:
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
