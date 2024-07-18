"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""


def isValid(s):

    # Dictionary to map opening brackets to their corresponding closing brackets
    d = {'(': ')', '{': '}', '[': ']'}
    
    # Initialize an empty stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the input string
    for i in s:

        # If the character is an opening bracket, push it onto the stack
        if i in d:
            stack.append(i)
        
        # If the character is a closing bracket
        else:

            # If the stack is empty (no corresponding opening bracket) or 
            # the closing bracket does not match the latest opening bracket, return False
            if len(stack) == 0 or d[stack.pop()] != i:
                return False
    
    # If the stack is empty after processing all characters, return True
    # (All opening brackets have been matched by corresponding closing brackets)
    return len(stack) == 0


# Test the function with an example
print(isValid('{}'))  # Output: True
