def syntax_checker(symbols):

	valid_syntax = {'(':')', '{':'}','[':']'}

	stack = []

	for symbol in symbols:

		if symbol in valid_syntax:

			stack.append(symbol)

		elif len(stack) == 0 or valid_syntax[stack.pop()] != symbol:

			return False

	return True


print(syntax_checker('({})'))