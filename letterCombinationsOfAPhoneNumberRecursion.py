# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

class Solution(object):
    def letterCombinations(self, digits):
        # hard coded phone letters with digits 
        phone = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}
        result = []
            
        # recursive helper 
        def recursiveCombineHelper(current, digits):
            if not digits: # this is the break point, if the digits passed are empty, append the last char and return
                result.append(current)
                return
            else:
                for char in phone[digits[0]]: # iterates through the amount of characters in the dictionary held by index 0 of digits
                    recursiveCombineHelper(current + char, digits[1:]) # makes the recursive call on the [1:] index making the problem smaller, and adds the char to current
            
        if not digits:
            return []
        else:
            recursiveCombineHelper("", digits)
            return result
