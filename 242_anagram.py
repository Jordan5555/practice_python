"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""


'Solution 1:'


def isAnagram(string1, string2):

    # Initialize dictionaries to count the frequency of each character in both strings
    string1_char_count = {}
    string2_char_count = {}

    # Count the frequency of each character in string1
    for char in string1:
        string1_char_count[char] = string1_char_count.get(char, 0) + 1

    # Count the frequency of each character in string2
    for char in string2:
        string2_char_count[char] = string2_char_count.get(char, 0) + 1

    # Compare the two dictionaries. If they are not equal, return False
    if string1_char_count != string2_char_count:
        return False

    # If the dictionaries are equal, return True
    return True




'Solution 2:'


def isAnagram(self, s: str, t: str) -> bool:
    # Convert both strings to lowercase and sort their characters
    # Return True if sorted versions of both strings are equal, otherwise return False
    return sorted(s.lower()) == sorted(t.lower())



'Solution 3:'


def isAnagram(string1, string2):
    
    # If lengths are different, they can't be anagrams
    if len(string1) != len(string2):
        return False

    # Initialize a dictionary to count character frequencies
    char_count = {}

    # Count characters in string1
    for char in string1:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract the count using characters from string2
    for char in string2:
        if char in char_count:
            char_count[char] -= 1
            # If count goes to zero, remove the character from the dictionary
            if char_count[char] == 0:
                del char_count[char]
        else:
            # If a character in string2 is not found in string1, they are not anagrams
            return False

    # If the dictionary is empty, all counts balanced out and the strings are anagrams
    return len(char_count) == 0

