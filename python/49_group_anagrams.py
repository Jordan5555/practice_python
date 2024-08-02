"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""


'Solution 1:'

def groupAnagrams(strs):

    # Check for an empty string
    if not strs:
        return [[""]]

    # Initialize an empty dictionary to hold the groups of anagrams
    groups = {}

    # Iterate over each word in the list of strings
    for word in strs:

        # Sort the letters of the word and use it as the key
        # Sorting ensures that all anagrams will have the same key
        key = "".join(sorted(word))

        # If the key is not already in the dictionary, add it with the word in a new list
        if key not in groups:
            groups[key] = [word]

        # If the key is already in the dictionary, append the word to the existing list
        else:
            groups[key].append(word)

    # Return the dictionary containing groups of anagrams
    return groups.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))