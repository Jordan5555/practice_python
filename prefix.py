"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""

words = ["Flower", "Flow", "Flight"]


def prefix_check(words):

	prefix = words[0]

	for i in words:

		while not i.startswith(prefix):

			prefix = prefix[:-1]

	return prefix

print(prefix_check(words))


def longestCommonPrefix(strs):

	a = min(strs)
	b = max(strs)

	j = 0

	while j < len(a) and j < len(b) and a[j] == b[j]:
		
		j += 1


	return a[:j]