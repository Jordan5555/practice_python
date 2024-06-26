# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


def wordPattern(pattern, s):

    # listOfStrings = s.split(' ')
    # list1 = []
    # list2 = []

    # for i in pattern:
    #     list1.append(pattern.index(i))

    # for i in listOfStrings:
    #     list2.append(listOfStrings.index(i))

    # if list1 == list2:
    #     return True
    # else:
    #     return False


    word = s.split()

    d1 = {}
    d2 = {}

    if len(pattern) != len(word):
        return False
            
    for key1, key2 in zip(pattern, word):
        if key1 in d1 and d1[key1] != key2 or key2 in d2 and d2[key2] != key1:
            return False

        d1[key1] = key2
        d2[key2] = key1

    return True

print(wordPattern("abba", "dog dog cat dog"))