# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


def isAnagram(s, t):

    s_counts = {}
    t_counts = {}

    for i in s:
    	
    	s_counts[i] = s_counts.get(i, 0) + 1

    for j in t:

        t_counts[j] = t_counts.get(j, 0) + 1

    if s_counts != t_counts:

        return False
        
    return True



    #  sorted_s = sorted(s)
    #     sorted_t = sorted(t)
    #     return sorted_s == sorted_t


print(isAnagram("anagram", "nagaram"))