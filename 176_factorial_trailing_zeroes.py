# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 104


def trailingZeroes(n):

    # Initialize zeros count to 0
    zeros_count = 0
    
    # Keep dividing n by 5 and update zeros count
    while n:
        n //= 5
        zeros_count += n
    
    # Return the count of trailing zeros in n!
    return zeros_count