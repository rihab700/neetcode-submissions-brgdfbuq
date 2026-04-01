class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        anagram =defaultdict(list)#it automatically creates a default value for a key if it doesn’t exist.
        for st in strs:
            count = [0]*26
            for c in st :
                count[ord(c)-ord("a")]+=1
            anagram[tuple(count)].append(st)#tuple cuz dict dosent accpet list as key
        return list(anagram.values())