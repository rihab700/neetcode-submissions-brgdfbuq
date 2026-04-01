class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapped_s = {}
        mapped_t = {}
        for i in range(len(s)):
            if s[i] in mapped_s:
                mapped_s[s[i]] +=1
            else:
                mapped_s[s[i]]=1
            if t[i] in mapped_t:
                mapped_t[t[i]] +=1
            else:
                mapped_t[t[i]]=1
        for s,v in mapped_s.items():
            if s not in mapped_t:
                return False
            elif v != mapped_t[s]:
                return False
        return True