# You are given three strings: s1, s2, and s3. In one operation you can choose one of these strings and delete its rightmost character. Note that you cannot completely empty a string.

# Return the minimum number of operations required to make the strings equal. If it is impossible to make them equal, return -1.

 

# Example 1:

# Input: s1 = "abc", s2 = "abb", s3 = "ab"

# Output: 2

# Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.

# Example 2:

# Input: s1 = "dac", s2 = "bac", s3 = "cac"

# Output: -1

# Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.

 

# Constraints:

# 1 <= s1.length, s2.length, s3.length <= 100
# s1, s2 and s3 consist only of lowercase English letters.



# Similar to problem 14:


def findMinimumOperations(s1, s2, s3):

        length_of_words = [s1, s2, s3]

        shortest_word = min(length_of_words)

        i = 0

        words_eligible = 0

        while i < len(shortest_word):

            if s1[i] == s2[i] == s3[i]:

                words_eligible += 1

            else:

                break

            i += 1

        if words_eligible == 0:

            return -1

        min_operation_count = sum(len(word) - words_eligible for word in length_of_words)

        return min_operation_count


        # words_list = [s1,s2,s3]

        # prefix = min(words_list)

        # for word in words_list:

        #     while not word.startswith(prefix):

        #         prefix = prefix[:-1]

        # if len(prefix) == 0:
            
        #     return -1

        # return sum(len(word) - len(prefix) for word in words_list)


print(findMinimumOperations(s1 = "dac", s2 = "bac", s3 = "cac"))