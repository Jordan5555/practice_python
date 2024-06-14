x = [1,2,3]

def add_numbers(list_numbers):

	num_string = ""

	for i in list_numbers:

		num_string += str(i)

	num_string = (int(num_string)) + 1

	num_string = str(num_string)

	output = []

	for j in num_string:

		output.append(int(j))

	return output

print(add_numbers(x))