# Input: s = "string"
# Output: "rtsng"


s = "poiinter"

def func(s):

    new_str = ""

    for i in range(len(s)):
        if s[i] == 'i': 
            new_str = s[:i][::-1] + s[i+1:] 
    return new_str

print(func(s))



