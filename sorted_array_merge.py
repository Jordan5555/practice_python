a = [1,2,3,4]

b = [4,5,6,7]


def merger(l1, l2):
	i = 0
	j = 0
	output = []

	while i < len(l1) and j < len(l2):

		if l1[i] < l2[j]:
			output.append(l1[i])
			i += 1

		else:
			output.append(l2[j])
			j += 1

	while i < len(l1):

		output.append(l1[i])
		i += 1

	while j < len(l2):

		output.append(l2[j])
		j += 1


	return output

print(merger(a,b))