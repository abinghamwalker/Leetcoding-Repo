"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    min_str = min(strs, key=len)
    for i, char in enumerate(min_str):
        for word in strs:
            if word[i] != char:
                return min_str[:i]

    return min_str

print(longestCommonPrefix(["flower","flow","flight"]))