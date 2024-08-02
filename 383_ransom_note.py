"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.


"""


'Solution 1:'


def func(ransomNote, magazine):
    
    # Initialize an empty dictionary to store the frequency of each character in the magazine
    magazine_dict = {}

    # Populate the dictionary with character frequencies from the magazine
    for char in magazine:
        magazine_dict[char] = magazine_dict.get(char, 0) + 1

    # Iterate through each character in the ransom note
    for char in ransomNote:

        # Check if the character is present in the magazine dictionary
        if char in magazine_dict and magazine_dict[char] > 0:

            # Decrease the count of the character in the dictionary
            magazine_dict[char] -= 1
            
        else:

            # If the character is not in the magazine dictionary, return False
            return False

    # If the loop completes, return True indicating the ransom note can be constructed
    return True




'Solution 2:'


def func(ransomNote, magazine):

    # Convert the magazine string into a list of characters
    magazine_list = list(magazine)

    # Iterate through each character in the ransom note
    for char in ransomNote:
        
        # Check if the character is in the magazine list
        if char in magazine_list:

            # If found, remove the character from the list to prevent reuse
            magazine_list.remove(char)
        
        else:

            # If the character is not found, return False
            return False

    # If all characters are found and removed, return True
    return True





