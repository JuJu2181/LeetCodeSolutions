class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #return false if the length differs 
        if len(s) != len(t):
            return False
        #initializing hashmaps
        mapST, mapTS = {},{} 
        #Loop through each character of both strings 
        for c1,c2 in zip(s,t):
            #check if the character exists in the hashmap and the mapping to character of next string also exist
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False 
            #perform mapping from one string to another 
            mapST[c1] = c2 
            mapTS[c2] = c1
        #if mapping is success for each character return True as it is isomorphic
        return True
    
if __name__ == "__main__":
    s1 = Solution()
    print(s1.isIsomorphic("egg","add"))
    print(s1.isIsomorphic("foo","bar"))
    print(s1.isIsomorphic("paper","title"))