"""

You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 108

"""


'Solution 1:'


def func(num):
    
    # Convert the input number to a string for easier manipulation
    str_num = str(num)

    # Calculate the minimum value by replacing all occurrences of the first digit with '0'
    minimum = int(str_num.replace(str_num[0], '0'))

    # Calculate the maximum value
    # Iterate over each character in the string representation of the number
    for index in str_num:

        # Find the first digit that is not '9'
        if index != '9':

            # Replace the first occurrence of this digit with '9'
            str_num = str_num.replace(index, '9')

            # Break the loop after the first replacement
            break
    
    # Convert the modified string back to an integer to get the maximum value
    maximum = int(str_num)

    # Return the difference between the maximum and minimum values
    return maximum - minimum


'Solution 2: produces wrong answer'

def maxDifference(num):
    # Convert the number to a string for easier manipulation
    str_num = str(num)
    
    # Initialize the maximum difference to 0
    max_diff = 0
    
    # Iterate over each digit from '0' to '9'
    for i in '0123456789':
        # Skip if the digit does not exist in the number
        if i not in str_num:
            continue
        
        # Iterate over each target digit from '0' to '9'
        for j in '0123456789':
            # Skip if the source digit is the same as the target digit
            if i == j:
                continue
            
            # Create the remapped number by replacing all occurrences of digit i with digit j
            remapped_num = str_num.replace(i, j)
            
            # Calculate the absolute difference
            diff = abs(int(remapped_num) - num)
            
            # Update the maximum difference if the current difference is larger
            max_diff = max(max_diff, diff)
    
    return max_diff
    

# Example usage
print(maxDifference(11891))  # Example output based on the problem description
