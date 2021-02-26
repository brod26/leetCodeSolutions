# Given a string s, return the longest palindromic substring in s.
# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Example 3:

# Input: s = "a"
# Output: "a"

# Example 4:

# Input: s = "ac"
# Output: "a"

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters (lower-case and/or upper-case),

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = [[0]*len(s) for i in range(len(s))]
        output = ""
        
        for i in range(len(s)):
            table[i][i] = True
            output = s[i]
        
        for column in (range(len(s)-1,-1,-1)):
            for row in range(column+1, len(s)):
                if s[column] == s[row]:
                    if row - column == 1 or table[column+1][row-1]:
                        table[column][row] = True
                        if len(output) < len(s[column:row+1]):
                            output = s[column:row+1]
        
        return output

