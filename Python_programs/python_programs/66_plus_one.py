"""

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

"""


'Solution 1: '


def plusOne(list_numbers):
	
	# Edge case: int will throw an error incase of empty string
	if not list_numbers:          
		return False

	# Initialize an empty list to store the output digits
	out = []

	# Initialize an empty string to concatenate the digits
	num_str = ""

	# Iterate through each number in the input list
	for num in list_numbers:
		
		# Convert each number to a string and concatenate it to num_str
		num_str += str(num)

	# Convert the concatenated string to an integer, add 1, and convert back to a string
	num_str = str(int(num_str) + 1)

	# Iterate through each character in the resulting string
	for i in num_str:
		
		# Convert each character back to an integer and append it to the output list
		out.append(int(i))

	# Return the output list which now represents the incremented number
	return out


'Solution 2: '

def plusOne(list_numbers):

    # Start from the end of the list and work backwards
    for i in reversed(range(len(list_numbers))):

        if list_numbers[i] < 9:

            # If the current digit is less than 9, simply increment it and return the result
            list_numbers[i] += 1
			
            return list_numbers
		
        # If the current digit is 9, set it to 0 and move to the next digit
        list_numbers[i] = 0

    # If we have finished the loop, it means all digits were 9
    # So we need to add a leading 1 at the beginning of the list
    return [1] + list_numbers




