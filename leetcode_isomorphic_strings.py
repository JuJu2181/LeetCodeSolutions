"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Using hashmap for solution
        #return false if the length differs 
        if len(s) != len(t):
            return False
        # initializing a dictionary to store letters from s and t as key value pairs
        charCount = {} 
        #iterating over s and t 
        for i in range(len(s)):
            #if s[i] is a key in charCount
            if s[i] in charCount:
                #get corresponding value for the key
                c = charCount[s[i]]
                #check with another string and return corresponding result
                if c != t[i]:
                    return False 
            #if t[i] is not a value in charCount 
            elif t[i] not in charCount.values():
                charCount[s[i]] = t[i]
            else:
                return False
        return True
    
if __name__ == "__main__":
    s1 = Solution()
    print(s1.isIsomorphic("egg","add"))
    print(s1.isIsomorphic("foo","bar"))
    print(s1.isIsomorphic("paper","title"))