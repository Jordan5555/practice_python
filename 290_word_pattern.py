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
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.


"""

'Solution 1:'


def wordPattern(s, pattern):

    # Split the input string s into a list of words
    s = s.split()
    
    # If the lengths of pattern and words are different, return False
    if len(pattern) != len(s):
        return False
    
    # Initialize two empty lists to store the indexes of each word and pattern character
    s_list = []
    pattern_list = []

    # Iterate over each word in the split string s
    for i in s:
        # Append the index of the first occurrence of the word in the list s to s_list
        s_list.append(s.index(i))

    # Iterate over each character in the pattern
    for i in pattern:
        # Append the index of the first occurrence of the character in the pattern to pattern_list
        pattern_list.append(pattern.index(i))

    # Return True if the two lists are the same, else return False
    return s_list == pattern_list




'Solution 2:'


def wordPattern(pattern, s):

    # Split the input string s into a list of words
    word = s.split()
    
    # If the lengths of pattern and words are different, return False
    if len(pattern) != len(word):
        return False

    # Initialize two dictionaries to store the mappings
    pattern_to_word = {}
    word_to_pattern = {}

    # Iterate through the pattern and words simultaneously
    for key1, key2 in zip(pattern, word):

        # If the pattern character is already mapped to a word, check if it matches the current word
        if key1 in pattern_to_word and pattern_to_word[key1] != key2 or key2 in word_to_pattern and word_to_pattern[key2] != key1:
            return False
    
        # Create the mapping from pattern to word and word to pattern
        pattern_to_word[key1] = key2
        word_to_pattern[key2] = key1

    # If all mappings are consistent, return True
    return True

print(wordPattern("abba", "dog dog cat dog"))