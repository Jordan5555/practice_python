"""

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


"""


def wordPattern(pattern, s):

    listOfStrings = s.split(' ')
    list1 = []
    list2 = []

    for i in pattern:
        list1.append(pattern.index(i))

    for i in listOfStrings:
        list2.append(listOfStrings.index(i))

    if list1 == list2:
        return True
    else:
        return False

print(wordPattern("abba", "dog cat cat dog"))