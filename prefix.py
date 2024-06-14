words = ["Flower", "Flow", "Flight"]


def prefix_check(words):

	prefix = words[0]

	for i in words:

		while not i.startswith(prefix):

			prefix = prefix[:-1]

	return prefix

print(prefix_check(words))