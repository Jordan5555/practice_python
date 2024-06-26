"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""


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



print(isAnagram("anagram", "nagaramd"))