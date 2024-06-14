# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#  

def reverseWords(s: str):	
    new_s = ''
    for i in s.split()[::-1]:
        new_s = new_s + ' ' + str(i)
    return new_s.strip()

print(reverseWords("a good   example"))
