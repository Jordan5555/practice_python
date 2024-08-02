"""

Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.

You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

Return the final string that will be present on your laptop screen.

 

Example 1:

Input: s = "string"
Output: "rtsng"
Explanation: 
After typing first character, the text on the screen is "s".
After the second character, the text is "st". 
After the third character, the text is "str".
Since the fourth character is an 'i', the text gets reversed and becomes "rts".
After the fifth character, the text is "rtsn". 
After the sixth character, the text is "rtsng". 
Therefore, we return "rtsng".
Example 2:

Input: s = "poiinter"
Output: "ponter"
Explanation: 
After the first character, the text on the screen is "p".
After the second character, the text is "po". 
Since the third character you type is an 'i', the text gets reversed and becomes "op". 
Since the fourth character you type is an 'i', the text gets reversed and becomes "po".
After the fifth character, the text is "pon".
After the sixth character, the text is "pont". 
After the seventh character, the text is "ponte". 
After the eighth character, the text is "ponter". 
Therefore, we return "ponter".
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
s[0] != 'i'


"""

'Solution 1: '


def finalString(s):

    """
    Processes the input string 's' such that every 'i' character reverses the current output string.
    All other characters are added to the output string as they are encountered.
    
    :param s: Input string
    :return: Processed string after all reversals
    """

    # Initialize the output string as empty
    out = ""  

    # Iterate through each character in the input string
    for char in s:

        if char != 'i':

            # If the character is not 'i', add it to the output string
            out += char

        else:
            
            # If the character is 'i', reverse the current output string
            out = out[::-1]

    # Return the final processed string
    return out  



'Solution 2: '



def finalString(s):

    # Initialize the pointers for iterating through the string
    left = 0
    right = 0

    # Initialize the output string
    out = ""

    # Iterate through the string using the right pointer
    while right < len(s) - 1:

        if s[right] != 'i':

            # If the current character is not 'i', move to the next character
            right += 1

        else:

            # Add the segment from left to right (exclusive) to the output
            out += s[left:right]

            # Reverse the current output string
            out = out[::-1]

            # Move the left pointer to the character after the current 'i'
            left = right + 1

            # Move to the next character after 'i'
            right += 1

    # Add the remaining segment after the last 'i' to the output
    return out + s[left:]

# Test the function with an example
print(finalString("poiinter"))




'Solution 3: '


def faulty(s):

    # Initialize the position index for iterating through the input string
    right = 0

    # Initialize an empty list to build the new string efficiently
    new = []

    # Loop through each character in the input string
    while right < len(s):

        if s[right] != "i":

            # If the current character is not 'i', append it to the new list
            new.append(s[right])

        else:

            # If the current character is 'i', reverse the current new list
            new.reverse()

        # Move to the next character in the input string
        right += 1

    # Join the list into a string and return it
    return ''.join(new)




 