# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"   


def vowels(s):

    head = 0
    tail = len(s)-1
    s = list(s) 
    vowels =  ['a', 'e', 'i', 'o', 'u']

    while (head < tail):            

        if s[head].lower() not in vowels:
            head += 1                
        
        elif s[tail].lower() not in vowels:
            tail -= 1
        
        else:    
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
            
    return "".join(s)


print(vowels("leetcode  "))