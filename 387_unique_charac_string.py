# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


def firstUniqChar(s):
	
    counts = {}

    for i in s:
    	
    	counts[i] = counts.get(i, 0) + 1

    for i in range(len(s)):

        if counts[s[i]] == 1:
            return i


    #   for i in s:
            
    #         counts[i] = counts.get(i, 0) + 1
            
    #     for key, val in counts.items():

    #         if val == 1:
    #             return s.index(key)

    #     return -1


    return -1

print(firstUniqChar("loveleetcode"))
