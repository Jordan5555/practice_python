"""

You are given three strings: s1, s2, and s3. In one operation you can choose one of these strings and delete its rightmost character. Note that you cannot completely empty a string.

Return the minimum number of operations required to make the strings equal. If it is impossible to make them equal, return -1.

 

Example 1:

Input: s1 = "abc", s2 = "abb", s3 = "ab"

Output: 2

Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.

Example 2:

Input: s1 = "dac", s2 = "bac", s3 = "cac"

Output: -1

Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.

 

Constraints:

1 <= s1.length, s2.length, s3.length <= 100
s1, s2 and s3 consist only of lowercase English letters.

"""

'Solution 1: '


def findMinimumOperations(s1, s2, s3):

    """
    Calculates the minimum number of operations required to make three strings identical
    by comparing their common prefix. If no common prefix exists, returns -1.

    :param s1: First string
    :param s2: Second string
    :param s3: Third string
    :return: Minimum number of operations or -1 if no common prefix
    """
    # List of input strings
    word_list = [s1, s2, s3]
    
    # Find the shortest string among the three to avoid index out-of-range errors
    min_word = min(word_list, key=len)
    
    # Initialize index for iteration and a counter for the common prefix length
    i = 0
    words_eligible = 0

    # Iterate through the characters of the shortest string
    while i < len(min_word):

        # Check if the characters at index i are the same for all strings
        if s1[i] == s2[i] == s3[i]:

            # Increment the common prefix length counter
            words_eligible += 1

        else:

            # Exit the loop if a mismatch is found
            break  

        i += 1  # Move to the next character index

    # If no common prefix is found, return -1
    if words_eligible == 0:
        return -1

    # Calculate the minimum operations needed to make all strings identical
    # by summing up the operations for each string
    min_operations = sum(len(word) - words_eligible for word in word_list)

    # Return the total minimum operations
    return min_operations  


'Solution 2: Similar to problem 14: '


def findMinimumOperations(s1, s2, s3):

    """
    Calculates the minimum number of operations required to make three strings identical
    by finding their common prefix. If no common prefix exists, returns -1.

    :param s1: First string
    :param s2: Second string
    :param s3: Third string
    :return: Minimum number of operations or -1 if no common prefix
    """
    words_list = [s1, s2, s3]
    
    # Start with the shortest string as the initial prefix
    prefix = min(words_list, key=len)

    # Iterate through each word to find the common prefix
    for word in words_list:

        # Reduce the prefix until the current word starts with it
        while not word.startswith(prefix):
            prefix = prefix[:-1]

    # If no common prefix is found, return -1
    if len(prefix) == 0:
        return -1

    # Calculate the minimum operations needed to make all strings identical
    # by summing up the operations for each string
    return sum(len(word) - len(prefix) for word in words_list)