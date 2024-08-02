"""

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


"""


'Solution 1:'



def strStr(haystack, needle):
    
	# An empty string is considered to be present at the beginning of any string.    
    if not needle: 
        return 0
    
	# If needle is longer than haystack
    elif len(needle) > len(haystack):  
        return -1

	# Checks if the substring starting at index "index" in haystack matches the entire needle.
    for index in range(len(haystack)):
        if haystack[index:index+len(needle)] == needle:
            return index

	# Return -1 if needle is not found in haystack
    return -1  



'Solution 2:'


def strStr(haystack, needle):
     
	# If needle is an empty string    
	if not needle: 
		return 0

	# If needle is longer than haystack
	elif len(needle) > len(haystack):  
		return -1
		
	# This condition checks if the substring needle exists within the string haystack.
	return -1 if needle not in haystack else haystack.index(needle)


print(strStr(haystack = "leetcode", needle = "leet"))


'Solution 3: '


def func(haystack, needle):
    
    # Initialize the left pointer to the start of the haystack
    left = 0  
    
    # Initialize the right pointer to the length of the needle
    right = len(needle)

    # Loop until the right pointer reaches the end of the haystack
    while right <= len(haystack):
        
        # Check if the current window in the haystack matches the needle
        if haystack[left:right] == needle:
            
            # If a match is found, return the starting index
            return left
        
        else:
            
            # If no match is found, move the window one character to the right
            left += 1
            right += 1

    # If the needle is not found in the haystack, return -1
    return -1

# Test the function with an example
print(func(haystack = "sadbutjunglesad", needle = "jungle"))

