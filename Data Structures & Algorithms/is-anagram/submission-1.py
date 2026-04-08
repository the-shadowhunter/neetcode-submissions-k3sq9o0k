class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch = {}
        if len(s) != len(t):
            return False
        for char in s:
            ch[char]= ch.get(char,0)+1

        for cha in t:
            if cha not in ch or ch[cha]==0:
                return False
            ch[cha]-=1
        return True
        