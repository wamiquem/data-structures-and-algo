# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Initialize hashmap for both strings
        sMap = {}
        tMap = {}
        
        #Initialize minWindowSize to infinity and result string to empty
        minWindowSize = float('inf')
        minWindow = ""
        
        #For string t, put every character frequency in tMap. This Map will never change after this.
        for ch in t:
            if ch in tMap:
                tMap[ch] += 1
            else:
                tMap[ch] = 1
        
        #Note the length of tMap. tMapSize will be used always to check if we got a substring that 
        #has all the characters of the string t
        tMapSize = len(tMap)
        
        #Initaialize a variable to hold the character and frequency match of sMap and tMap
        sMapMatch = 0
        
        #Initialize left and right pointer for the window
        #Intuition for sliding window is that until we have found a substring in s that has 
        #all characters of t, we go on incrementing r. Once we have found such a substring, we do not know 
        #whether this is minimum window, so we go on incrementing l.
        l,r = 0, 0
        while r< len(s):
            #Get a character from s
            curr = s[r]

            #add it along with its frequency in the sMap
            if curr in sMap:
                sMap[curr] += 1
            else:
                sMap[curr] = 1

            #Immediately after a character is added in the sMap, check if the same character exists in tMap.
            #If it exists, check if its frequency is same in both the maps. If yes, it means that the current
            #character now exists in the substring. Increment the sMapMatch.
            if curr in tMap and tMap[curr] == sMap[curr]:
                sMapMatch += 1
            
            #if sMapMatch becomes equal to tMapSize, it implies that each and every character of t now exists 
            #in the current window, if current window size < minWindowSize, we change the minWindowSize and 
            #update the result with the current Window.
            #Also, once we used the current window, it means we need to increment l. But before that, as we are moving 
            #our window's left index right by 1, we need to adjust the character's frequency at l in sMap.
            #We need to further adjust sMapMatch(decrement by 1) if this character also exists in t.
            while tMapSize == sMapMatch:
                if r-l+1 < minWindowSize:
                    minWindowSize = r-l+1
                    minWindow = s[l:r+1]
                sMap[s[l]] -= 1
                if s[l] in tMap and tMap[s[l]] > sMap[s[l]]:
                    sMapMatch -= 1
                l += 1
                
            r += 1
        return minWindow