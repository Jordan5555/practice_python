"""

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""



def wordBreak(s, wordDict):
    
    # Convert wordDict to a set for faster look-up
    word_set = set(wordDict)
    
    # Initialize the DP array with False
    dp = [False] * (len(s) + 1)
    
    # Empty string can always be segmented
    dp[0] = True
    
    # Iterate over the length of the string
    for i in range(1, len(s) + 1):

        # Check all substrings ending at i
        for j in range(i):

            # If the substring s[j:i] is in word_set and the substring s[0:j] can be segmented,
            # set dp[i] to True and break out of the loop
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    # Return the value for the entire string
    return dp[len(s)]
