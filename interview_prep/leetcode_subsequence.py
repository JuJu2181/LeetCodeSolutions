"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #initially set the two pointers to beggining of strings
        i,j = 0,0
        #loop through both the strings upto their end
        while i < len(s) and j < len(t):
            #if a character in s is matched in t increment the ith pointer to search for next character in s 
            if s[i] == t[j]:
                i += 1
            #check for each character in t by incrementing the value of j 
            j += 1
        
        #if the value of i reaches to the length of s it means that all the characters in s were found in t, so it means s is a subsequence of t and hence we return True else False
        return True if i == len(s) else False
    
if __name__=="__main__":
    s1 = Solution()
    print(s1.isSubsequence("abc","ahbgdc"))
    print(s1.isSubsequence("axc","ahbgdc"))
    