"""
9. Palindrome Number
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

def isPalindrome(x):
    
    string_x = str(x)
    start = 0
    end = len(string_x) - 1


    while start < end:
        if string_x[start] != string_x[end]:
            return False
        start += 1
        end -= 1
    return True
    

print(isPalindrome(121))

