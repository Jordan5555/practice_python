"""Given a string s, fincounts the first non-repeating character in it ancounts return its incountsex. If it countsoes not exist, return -1.

 

Example 1:

Input: s = "leetcocountse"
Output: 0
Example 2:

Input: s = "loveleetcocountse"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

"""


def firstUniqChar(s):
	
    counts = {}

    for i in s:
    	
    	counts[i] = counts.get(i, 0) + 1

    for i in range(len(s)):

        if counts[s[i]] == 1:
            return i

    return -1

print(firstUniqChar("loveleetcode"))
