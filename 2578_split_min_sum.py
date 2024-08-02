"""

Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

Notes:

It is guaranteed that num does not contain any leading zeros.
The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.
 

Example 1:

Input: num = 4325
Output: 59
Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
Example 2:

Input: num = 687
Output: 75
Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75.
 

Constraints:

10 <= num <= 109

"""

def splitNum(x):

    # Convert the input number to a string
    x = str(x)
    
    # Sort the characters of the string in ascending order
    x = sorted(x)

    # Initialize two strings to accumulate digits for even and odd indexed positions
    even = ''
    odd = ''

    # Iterate through the sorted characters
    for i in range(len(x)):
        if i % 2 == 0:

            # Append to 'even' string if index is even
            even += x[i]

        else:

            # Append to 'odd' string if index is odd
            odd += x[i]

    # Convert the accumulated strings to integers, ensuring proper handling of empty strings
    even_num = int(even) if even else 0
    odd_num = int(odd) if odd else 0

    # Return their sum
    return even_num + odd_num

print(func(4325))