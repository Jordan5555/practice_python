"""

You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

 

Example 1:

Input: words = ["are","amy","u"], left = 0, right = 2
Output: 2
Explanation: 
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
The number of vowel strings in the mentioned range is 2.
Example 2:

Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
Output: 3
Explanation: 
- "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
- "mu" is not a vowel string because it does not start with a vowel.
- "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
- "artro" is a vowel string because it starts with 'a' and ends with 'o'.
The number of vowel strings in the mentioned range is 3.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 10
words[i] consists of only lowercase English letters.
0 <= left <= right < words.length


"""


def vowelStrings(words, left, right):
    """
    Counts the number of words that start and end with a vowel in a given sublist.
    
    :param words: List[str] - List of words to check
    :param left: int - Starting index of the sublist
    :param right: int - Ending index of the sublist
    :return: int - Count of words starting and ending with a vowel
    """
    count = 0  # Initialize the count of words starting and ending with a vowel
    
    # Iterate through the specified sublist of words
    for i in words[left : right + 1]:

        # Check if the word starts and ends with a vowel
        if i.startswith(('a', 'e', 'i', 'o', 'u')) and i.endswith(('a', 'e', 'i', 'o', 'u')):
            
            # Increment the count if both conditions are satisfied
            count += 1  
            
    return count  # Return the final count



# Example usage
print(vowelStrings(["are", "amy", "u"], 0, 2))  # Expected output: 2

# Additional edge cases
# Case with an empty list
print(vowelStrings([], 0, 0))  # Expected output: 0

# Case with a single word that starts and ends with a vowel
print(vowelStrings(["apple"], 0, 0))  # Expected output: 1

# Case with a single word that does not start and end with a vowel
print(vowelStrings(["banana"], 0, 0))  # Expected output: 0

# Case with multiple words, all starting and ending with a vowel
print(vowelStrings(["apple", "orange", "umbrella"], 0, 2))  # Expected output: 3

# Case with no words starting and ending with a vowel
print(vowelStrings(["dog", "cat", "fish"], 0, 2))  # Expected output: 0

# Case with mixed starting and ending vowels
print(vowelStrings(["apple", "banana", "ice", "orange"], 0, 3))  # Expected output: 2

# Case with sublist that includes words not starting and ending with a vowel
print(vowelStrings(["apple", "banana", "ice", "orange"], 1, 3))  # Expected output: 1


print(vowelStrings(["are","amy","u"], 0, 2))