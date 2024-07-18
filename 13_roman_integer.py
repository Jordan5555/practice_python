"""

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].


"""


'Solution 1:'

   
def romanToInt(s):

    # Dictionary mapping Roman numerals to their integer values
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    # Initialize the resulting integer value to 0
    number = 0

    # Loop through the string 's', stopping at the second to last character
    for index in range(len(s) - 1):

        # If the current Roman numeral is less than the next one, subtract its value
        if roman[s[index]] < roman[s[index + 1]]:
            number -= roman[s[index]]
            
        # Otherwise, add its value
        else:
            number += roman[s[index]]
    
    # Add the value of the last Roman numeral
    return number + roman[s[-1]]

# Example usage:
print(romanToInt("XIV"))  # Output: 14




'Solution 2:'


def romanToInt(s):

    # Dictionary mapping Roman numerals to their integer values
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Initialize the resulting integer value to 0
    number = 0

    # Replace subtractive combinations with equivalent additive ones
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    # Loop through each character in the modified string
    for char in s:

        # Add the value of each Roman numeral to 'number'
        number += translations[char]
    
    # Return the final computed integer value
    return number

# Example usage:
print(romanToInt("MCMXCIV"))  # Output: 1994
