"""

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

"""

'Solution 1:'


def mergeAlternately(word1, word2):

    # Initialize pointers for word1 and word2
    i = 0
    j = 0 
    
    # Initialize an empty string to store the merged result
    new = ""

    # Merge characters alternately until one of the words is exhausted
    while i < len(word1) and j < len(word2):

        # Append character from word1
        new += word1[i]

        # Append character from word2
        new += word2[j]

        # Move to the next character in word1
        i += 1

        # Move to the next character in word2
        j += 1

    # Append remaining characters from word1, if any
    while i < len(word1):
        new += word1[i]
        i += 1

    # Append remaining characters from word2, if any
    while j < len(word2):
        new += word2[j]
        j += 1

    return new



'Solution 2:'


from itertools import zip_longest

def mergeAlternately(word1, word2):

    # Use zip_longest to iterate over word1 and word2 alternately
    return "".join((a+b for a, b in zip_longest(word1, word2, fillvalue="")))